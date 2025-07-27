# ======================================
# ✅ MegaBot Final - handlers/io_handler.py
# /io komutu - In-Out Alış Satış Baskısı raporu
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_io_report

async def io_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = get_io_report()
    await update.message.reply_text(report)

def register_io(app):
    from telegram.ext import CommandHandler
    app.add_handler(CommandHandler("io", io_command))
