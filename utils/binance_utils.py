# ✅ Binance API'den veri çekme
# ======================================
# ✅ MegaBot Final - utils/binance_utils.py
# Binance API'den veri çekme, IO, NLS, NPR, AP, fiyat, FR, Whale fonksiyonları
# ======================================
import aiohttp
import math

BASE_URL = "https://api.binance.com/api/v3"
FUTURES_URL = "https://fapi.binance.com/fapi/v1"

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as response:
            return await response.json()

# ---------------- IO (In-Out) ----------------
async def get_io_report(coins):
    results = []
    for coin in coins:
        symbol = coin.upper() + "USDT"
        data = await fetch_json(f"{BASE_URL}/ticker/24hr?symbol={symbol}")
        buy_ratio = round((float(data["quoteVolume"]) / float(data["volume"])) % 100, 2)
        sell_ratio = 100 - buy_ratio
        results.append(f"{coin.upper()}: 🟢{buy_ratio}% / 🔻{sell_ratio}%")
    return "📊 IO Raporu\n" + "\n".join(results)

# ---------------- NLS (Balina yoğunluğu) ----------------
async def get_nls_report(coins):
    results = []
    for coin in coins:
        symbol = coin.upper() + "USDT"
        data = await fetch_json(f"{FUTURES_URL}/depth?symbol={symbol}&limit=20")
        bids = sum(float(x[1]) for x in data["bids"])
        asks = sum(float(x[1]) for x in data["asks"])
        ratio = round((bids / (bids + asks)) * 100, 2)
        results.append(f"{coin.upper()}: 🟢{ratio}% Long / 🔻{100 - ratio}% Short")
    return "📊 NLS Raporu\n" + "\n".join(results)

# ---------------- NPR (Nakit Piyasa Raporu) ----------------
async def get_npr_report(interval="1h"):
    data = await fetch_json(f"{FUTURES_URL}/premiumIndex")
    shorts = [float(x["lastFundingRate"]) for x in data]
    avg = round(sum(shorts) / len(shorts) * 100, 3)
    trend = "🔻 Short Baskısı" if avg < 0 else "🟢 Long Baskısı"
    return f"📊 NPR ({interval})\nOrtalama Funding Rate: {avg}%\n{trend}"

# ---------------- ETF & ABD ----------------
async def get_eft_report():
    return "📊 ETF & ABD Raporu\n(Bu örnek rapor, gerçek API entegre edilebilir.)"

# ---------------- AP (Alt Strength Index) ----------------
async def get_ap_report(mode="default"):
    data = await fetch_json(f"{BASE_URL}/ticker/24hr")
    altcoins = [x for x in data if x["symbol"].endswith("USDT") and not x["symbol"].startswith("BTC")]
    avg_change = sum(float(x["priceChangePercent"]) for x in altcoins) / len(altcoins)
    trend = "🟢 Yükseliş" if avg_change > 0 else "🔻 Düşüş"
    return f"📊 AP (Altların Güç Endeksi)\nGenel Değişim: {round(avg_change,2)}%\nTrend: {trend}"

# ---------------- Price ----------------
async def get_price_report(coins):
    results = []
    for coin in coins:
        symbol = coin.upper() + "USDT"
        data = await fetch_json(f"{BASE_URL}/ticker/24hr?symbol={symbol}")
        price = float(data["lastPrice"])
        change = float(data["priceChangePercent"])
        vol = float(data["quoteVolume"]) / 1_000_000
        arrow = "🔼" if change >= 0 else "🔻"
        results.append(f"{coin.upper()}: {price} {arrow}{change}% (Vol: {round(vol,2)}M$)")
    return "\n".join(results)

# ---------------- FR (Funding Rate) ----------------
async def get_fr_report(coins):
    data = await fetch_json(f"{FUTURES_URL}/premiumIndex")
    filtered = [x for x in data if not coins or x["symbol"].replace("USDT","").lower() in [c.lower() for c in coins]]
    top10 = sorted(filtered, key=lambda x: abs(float(x["lastFundingRate"])), reverse=True)[:10]
    lines = [f"{x['symbol']}: {round(float(x['lastFundingRate'])*100,3)}%" for x in top10]
    avg = round(sum(float(x["lastFundingRate"]) for x in filtered) / len(filtered) * 100,3)
    return f"📊 Funding Rate Raporu (Top10)\n" + "\n".join(lines) + f"\n\nGenel Ortalama: {avg}%"

# ---------------- Whale Alerts ----------------
async def get_whale_report(coins):
    results = []
    for coin in coins if coins else ["BTC","ETH"]:
        symbol = coin.upper() + "USDT"
        data = await fetch_json(f"{FUTURES_URL}/trades?symbol={symbol}&limit=20")
        big_trades = [float(x["qty"]) for x in data if float(x["quoteQty"])>1_000_000]
        total = sum(big_trades)
        results.append(f"{coin.upper()}: {round(total,2)} {coin.upper()} ({round(total*float(data[0]['price']),2)}$)")
    return "🐋 Whale Alerts\n" + "\n".join(results)
