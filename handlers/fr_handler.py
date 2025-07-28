# ======================================
# ✅ MegaBot Final - handlers/fr_handler.py
# /fr komutu - Funding Rate raporu (gerçek Binance verisi)
# ======================================
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_fr_report

async def fr_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coins = context.args if context.args else []
    report = await get_fr_report(coins)
    await update.message.reply_text(report)

def register_fr_handlers(app):
    app.add_handler(CommandHandler("fr", fr_command))
