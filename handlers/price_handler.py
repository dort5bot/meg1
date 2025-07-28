# /p → Anlık fiyat, 24h değişim, hacim bilgisi
# ======================================
# ✅ MegaBot Final - handlers/price_handler.py
# /p komutu - Anlık fiyat, 24h değişim, hacim bilgisi
# ======================================

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.binance_utils import get_price_report

async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbols = context.args if context.args else ["BTC", "ETH"]
    report = get_price_report(symbols)
    await update.message.reply_text(report)

def register_price(application):
    application.add_handler(CommandHandler("p", price_command))
