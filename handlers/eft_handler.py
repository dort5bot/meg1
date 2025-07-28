# /eft → ETF & ABD piyasaları
# ======================================
# ✅ MegaBot Final - handlers/eft_handler.py
# /eft komutu - ETF & ABD Piyasaları
# ======================================

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_etf_report

async def eft_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = get_etf_report()
    await update.message.reply_text(report)

def register_eft(application):
    application.add_handler(CommandHandler("eft", eft_command))
