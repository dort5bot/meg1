
# ======================================
# ✅ MegaBot Final - handlers/price_handler.py
# /p komutu - Anlık fiyat, 24 saat değişim ve hacim bilgisi
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_price_report

async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coins = context.args
    if not coins:
        await update.message.reply_text("Lütfen en az bir coin sembolü yazınız, örn: /p btc eth")
        return

    report = get_price_report(coins)
    await update.message.reply_text(report)


def register_price(app):
    from telegram.ext import CommandHandler
    app.add_handler(CommandHandler("p", price_command))