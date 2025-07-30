
# ======================================
# ✅ MegaBot Final - handlers/ap_handler.py
# /ap komutu - Altların Güç Endeksi (AP)
# ======================================

from telegram import Update
from telegram.ext import ContextTypes
from utils.binance_utils import get_ap_report
from utils.csv_utils import save_ap_csv
import datetime

async def ap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report_data = get_ap_report()
    save_ap_csv(report_data)  # CSV kaydı

    msg = (
        f"📊 AP (Altların Güç Endeksi)\n"
        f"Kısa Vadede BTC'ye Karşı Güç: {report_data['short_btc']:.2f}\n"
        f"Kısa Vadede USD Gücü: {report_data['short_usd']:.2f}\n"
        f"Uzun Vadede Altların Gücü: {report_data['long_term']:.2f}\n\n"
    )

    # Basit yorumlama
    ap_val = report_data['long_term']
    if ap_val > 60:
        trend = "Altlar güçlü, BTC'ye karşı baskın."
    elif 40 < ap_val <= 60:
        trend = "Nötr, yönsüz piyasa."
    else:
        trend = "BTC güçlü, altlar zayıf."

    msg += f"Trend Yorumu: {trend}"

    await update.message.reply_text(msg)


async def ap_daily_job(context: ContextTypes.DEFAULT_TYPE):
    report_data = get_ap_report()
    save_ap_csv(report_data)
    print("✅ AP günlük kayıt alındı")


def register_ap(app):
    from telegram.ext import CommandHandler
    from datetime import time

    app.add_handler(CommandHandler("ap", ap_command))

    # Günlük JobQueue kaydı TSI 03:05
    app.job_queue.run_daily(
        ap_daily_job,
        time=time(hour=0, minute=5),
        name="ap_daily"
    )