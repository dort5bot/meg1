# ======================================
# ✅ MegaBot Final - handlers/fr_handler.py
# /fr komutu - Funding Rate raporu + günlük CSV kaydı
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_funding_rate
from utils.csv_utils import save_funding_rate_csv
import datetime

async def fr_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rates = get_funding_rate()
    save_funding_rate_csv(rates)

    msg = "📊 Funding Rate Raporu (Top 10)\n"
    total_rate = 0

    for r in rates:
        direction = "🔼" if r["fundingRate"] > 0 else "🔻"
        total_rate += r["fundingRate"]
        msg += f"{r['symbol']}: {r['fundingRate']*100:.3f}% {direction}\n"

    avg_rate = total_rate / len(rates)
    yorum = "Long yönlü baskı artıyor" if avg_rate > 0 else "Short yönlü baskı artıyor"

    msg += f"\nGenel Ortalama: {avg_rate*100:.3f}% {'🔼' if avg_rate>0 else '🔻'}\n"
    msg += f"Yorum: {yorum}"

    await update.message.reply_text(msg)


async def fr_daily_job(context: ContextTypes.DEFAULT_TYPE):
    rates = get_funding_rate()
    save_funding_rate_csv(rates)
    print("✅ Funding Rate günlük kayıt alındı")


def register_fr(app):
    from telegram.ext import CommandHandler
    from datetime import time

    app.add_handler(CommandHandler("fr", fr_command))

       # Günlük kayıt (TSI 03:05)
    app.job_queue.run_daily(
        fr_daily_job,
        time=time(hour=0, minute=5),
        name="fr_daily"
    )

