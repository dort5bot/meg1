# /nls → Balina hareketleri ve yoğunluk (NLS analizi)
# ======================================
# ✅ MegaBot Final - handlers/nls_handler.py
# /nls komutu - Balina Yoğunluğu (NLS)
# ======================================

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_nls_report

async def nls_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coins = context.args if context.args else ["BTC"]
    report = await get_nls_report(coins)
    await update.message.reply_text(report)

def register_nls_handlers(app):
    app.add_handler(CommandHandler("nls", nls_command))