
# ======================================
# ✅ MegaBot Final - utils/binance_utils.py
# Binance verilerini çeken fonksiyonlar (IO, NLS, NPR, AP, Fiyat, FR, Whale)
# ======================================

import requests

BASE_URL = "https://api.binance.com/api"

def get_price_report(coins):
    msg = ""
    for coin in coins:
        symbol = coin.upper() + "USDT"
        try:
            res = requests.get(f"{BASE_URL}/v3/ticker/24hr", params={"symbol": symbol}).json()
            price = float(res["lastPrice"])
            change = float(res["priceChangePercent"])
            vol = float(res["quoteVolume"]) / 1_000_000

            if int(price) == 0:
                price_fmt = f"{price:.8f}"
            else:
                price_fmt = f"{price:.2f}"

            arrow = "🔼" if change > 0 else "🔻"
            msg += f"{symbol.replace('USDT','')}: {price_fmt} {arrow}{change:.3f}% (Vol: {vol:.1f}M$)\n"
        except:
            msg += f"{coin.upper()}: Veri alınamadı\n"
    return msg.strip()


def get_io_report():
    return "📊 IO Raporu (Mock) - Gerçek hesaplama burada entegre edilecek."


def get_nls_report():
    return "📊 NLS Raporu (Mock)"


def get_npr_report():
    return "📊 NPR Raporu (Mock)"


def get_etf_report():
    return "📊 ETF & ABD Raporu (Mock)"


def get_ap_report():
    # Mock değerler (örnek)
    return {
        "short_btc": 13.2,
        "short_usd": 29.1,
        "long_term": 57.5
    }


def get_funding_rate():
    try:
        res = requests.get("https://fapi.binance.com/fapi/v1/premiumIndex").json()
        sorted_rates = sorted(res, key=lambda x: abs(float(x["lastFundingRate"])), reverse=True)[:10]
        return [
            {
                "symbol": r["symbol"],
                "fundingRate": float(r["lastFundingRate"])
            }
            for r in sorted_rates
        ]
    except:
        return []


def get_whale_alerts():
    # NOT: Gerçek Whale Alerts için 3. parti API gerekir.
    # Şimdilik MOCK veri
    return [
        {"symbol": "BTC", "amount": 120.5, "asset": "BTC", "usd": 7000000, "side": "buy"},
        {"symbol": "ETH", "amount": 1500, "asset": "ETH", "usd": 2700000, "side": "sell"}
    ]