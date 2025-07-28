# ======================================
# ✅ MegaBot Final - handlers/io_handler.py
# /io komutu - In-Out Alış Satış Baskısı (gerçek Binance verisi)
# ======================================
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_io_report

async def io_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coins = context.args if context.args else ["BTC"]
    report = await get_io_report(coins)
    await update.message.reply_text(report)

def register_io_handlers(app):
    app.add_handler(CommandHandler("io", io_command))
