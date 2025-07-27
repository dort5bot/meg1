# ======================================
# ✅ MegaBot Final - handlers/nls_handler.py
# /nls komutu - Balina hareketleri ve yoğunluk (NLS analizi)
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_nls_report

async def nls_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = get_nls_report()
    await update.message.reply_text(report)

def register_nls(app):
    from telegram.ext import CommandHandler
    app.add_handler(CommandHandler("nls", nls_command))
