
# ======================================
# ✅ MegaBot Final - utils/csv_utils.py
# CSV okuma/yazma, 60 kayıt sınırı, FR ve Whale CSV kayıtları
# ======================================

import csv, os, datetime

def save_csv(file, row):
    rows = []
    if os.path.exists(file):
        with open(file, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            rows = reader[1:] if reader else []

    rows.append(row)
    if len(rows) > 60:
        rows = rows[-60:]

    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp"] + [f"c{i}" for i in range(len(row) - 1)])
        writer.writerows(rows)


def save_ap_csv(data):
    row = [datetime.datetime.utcnow().isoformat(), data["short_btc"], data["short_usd"], data["long_term"]]
    save_csv("data/ap_history.csv", row)


def save_funding_rate_csv(rates):
    avg = sum([r["fundingRate"] for r in rates]) / len(rates) if rates else 0
    row = [datetime.datetime.utcnow().isoformat(), avg]
    save_csv("data/fr_history.csv", row)


def save_whale_csv(alerts):
    total_usd = sum([a["usd"] for a in alerts])
    row = [datetime.datetime.utcnow().isoformat(), total_usd]
    save_csv("data/whale_history.csv", row)