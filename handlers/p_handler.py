# ======================================
# ✅ MegaBot Final - handlers/p_handler.py
# /p_ekle, /p_fav, /p_sil komutları - Favori coin listesi yönetimi
# ======================================
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.csv_utils import add_favorite, remove_favorite, list_favorites

async def p_ekle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coins = context.args
    if not coins:
        await update.message.reply_text("⚠️ Kullanım: /p_ekle BTC ETH")
        return
    add_favorite(update.effective_user.id, coins)
    await update.message.reply_text(f"✅ Favorilere eklendi: {', '.join(coins)}")

async def p_sil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coins = context.args
    if not coins:
        await update.message.reply_text("⚠️ Kullanım: /p_sil BTC ETH")
        return
    remove_favorite(update.effective_user.id, coins)
    await update.message.reply_text(f"🗑 Silindi: {', '.join(coins)}")

async def p_fav(update: Update, context: ContextTypes.DEFAULT_TYPE):
    favs = list_favorites(update.effective_user.id)
    await update.message.reply_text(f"⭐ Favorileriniz: {', '.join(favs) if favs else 'Yok'}")

def register_p_handlers(app):
    app.add_handler(CommandHandler("p_ekle", p_ekle))
    app.add_handler(CommandHandler("p_sil", p_sil))
    app.add_handler(CommandHandler("p_fav", p_fav))
