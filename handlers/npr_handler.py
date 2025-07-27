# ======================================
# ✅ MegaBot Final - handlers/npr_handler.py
# /npr komutu - Nakit Piyasa Raporu
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_npr_report

async def npr_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = get_npr_report()
    await update.message.reply_text(report)

def register_npr(app):
    from telegram.ext import CommandHandler
    app.add_handler(CommandHandler("npr", npr_command))
