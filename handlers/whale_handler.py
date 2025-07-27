# ======================================
# ✅ MegaBot Final - handlers/whale_handler.py
# /whale komutu - Whale Alerts raporu + günlük CSV kaydı
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_whale_alerts
from utils.csv_utils import save_whale_csv
import datetime

async def whale_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    alerts = get_whale_alerts()
    save_whale_csv(alerts)

    msg = "🐋 Whale Alerts (Son 10 büyük işlem)\n"
    for a in alerts:
        emoji = "🔴" if a["side"] == "sell" else "🟢"
        msg += f"{a['symbol']}: {a['amount']:.2f} {a['asset']} ({a['usd']:.2f}$) {emoji}\n"

    await update.message.reply_text(msg)


async def whale_daily_job(context: ContextTypes.DEFAULT_TYPE):
    alerts = get_whale_alerts()
    save_whale_csv(alerts)
    print("✅ Whale Alerts günlük kayıt alındı")


def register_whale(app):
    from telegram.ext import CommandHandler
    from datetime import time

    app.add_handler(CommandHandler("whale", whale_command))

    # Günlük kayıt (TSI 03:05)
    app.job_queue.run_daily(
        whale_daily_job,
        time=time(hour=0, minute=5),
        name="whale_daily"
    )
