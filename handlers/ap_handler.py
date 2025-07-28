# ======================================
# ✅ MegaBot Final - handlers/ap_handler.py
# /ap komutu - Altların Güç Endeksi (gerçek Binance verisi)
# ======================================
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_ap_report

async def ap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = "trend" if "trend" in context.args else "default"
    report = await get_ap_report(mode)
    await update.message.reply_text(report)

def register_ap_handlers(app):
    app.add_handler(CommandHandler("ap", ap_command))
