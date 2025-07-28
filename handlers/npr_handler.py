# /npr → Nakit Piyasa Raporu
# ======================================
# ✅ MegaBot Final - handlers/npr_handler.py
# /npr komutu - Nakit Piyasa Raporu (gerçek Binance verisi)
# ======================================
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_npr_report

async def npr_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    interval = context.args[0] if context.args else "1h"
    report = await get_npr_report(interval)
    await update.message.reply_text(report)

def register_npr_handlers(app):
    app.add_handler(CommandHandler("npr", npr_command))

