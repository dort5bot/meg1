# ======================================
# ✅ MegaBot Final - handlers/whale_handler.py
# /whale komutu - Whale Alerts raporu (gerçek Binance verisi)
# ======================================
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_whale_report

async def whale_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coins = context.args if context.args else []
    report = await get_whale_report(coins)
    await update.message.reply_text(report)

def register_whale_handlers(app):
    app.add_handler(CommandHandler("whale", whale_command))
