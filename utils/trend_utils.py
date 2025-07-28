# ✅ Trend okları ve yüzde değişim hesaplama
# ======================================
# ✅ MegaBot Final - utils/trend_utils.py
# Trend okları, yüzde değişim hesaplama ve formatlama
# ======================================
def trend_arrow(value):
    return "🔼" if value >= 0 else "🔻"

def percent_format(value):
    return f"{'+' if value>=0 else ''}{round(value,2)}%"
