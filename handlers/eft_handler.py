# ======================================
# ✅ MegaBot Final - handlers/eft_handler.py
# /eft komutu - ETF & ABD piyasaları raporu
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_eft_report

async def eft_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = get_eft_report()
    await update.message.reply_text(report)

def register_eft(app):
    from telegram.ext import CommandHandler
    app.add_handler(CommandHandler("eft", eft_command))
