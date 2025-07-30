# ======================================
# ✅ MegaBot Final - handlers/etf_handler.py
# /etf komutu - ETF & ABD piyasaları raporu
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_etf_report  # düzeltildi: get_eft_report → get_etf_report

async def etf_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = get_etf_report()
    await update.message.reply_text(report)

def register_etf(app):
    from telegram.ext import CommandHandler
    app.add_handler(CommandHandler("etf", etf_command))  # komut da /etf oldu
