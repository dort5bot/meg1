# ======================================
# ✅ MegaBot Final - handlers/p_handler.py
# /p_ekle, /p_fav, /p_sil komutları - Favori coin listesi yönetimi ve hızlı butonlar
# ======================================

import json
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler

FAV_FILE = "data/fav_list.json"

def load_fav_lists():
    if not os.path.exists(FAV_FILE):
        return {}
    with open(FAV_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_fav_lists(data):
    with open(FAV_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

async def p_add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Kullanım: /p_ekle F1 btc eth ...")
        return

    fav_name = args[0].upper()
    coins = [c.lower() for c in args[1:]]

    data = load_fav_lists()
    data[fav_name] = coins
    save_fav_lists(data)

    await update.message.reply_text(f"Favori listesi {fav_name} eklendi/güncellendi: {', '.join(coins)}")


async def p_fav(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_fav_lists()
    if not data:
        await update.message.reply_text("Favori listesi yok.")
        return

    keyboard = []
    for name in sorted(data.keys()):
        keyboard.append([InlineKeyboardButton(name, callback_data=f"fav_{name}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Favori listeler:", reply_markup=reply_markup)


async def p_fav_button(update, context):
    query = update.callback_query
    await query.answer()
    fav_name = query.data.split("_", 1)[1]

    data = load_fav_lists()
    coins = data.get(fav_name)
    if not coins:
        await query.edit_message_text("Liste bulunamadı.")
        return

    from utils.binance_utils import get_price_report
    report = get_price_report(coins)
    await query.edit_message_text(report)


async def p_delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 1:
        await update.message.reply_text("Kullanım: /p_sil F1")
        return

    fav_name = args[0].upper()
    data = load_fav_lists()
    if fav_name in data:
        del data[fav_name]
        save_fav_lists(data)
        await update.message.reply_text(f"{fav_name} favori listesi silindi.")
    else:
        await update.message.reply_text(f"{fav_name} bulunamadı.")


def register_p(app):
    app.add_handler(CommandHandler("p_ekle", p_add))
    app.add_handler(CommandHandler("p_fav", p_fav))
    app.add_handler(CommandHandler("p_sil", p_delete))
    app.add_handler(CallbackQueryHandler(p_fav_button, pattern=r"fav_.*"))
