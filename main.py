
# ======================================
# ✅ MegaBot Final - main.py
# Ana bot başlatma, handler kayıtları, JobQueue görevleri
# ======================================

import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

from handlers.io_handler import register_io
from handlers.nls_handler import register_nls
from handlers.npr_handler import register_npr
from handlers.etf_handler import register_etf
from handlers.ap_handler import register_ap
from handlers.price_handler import register_price
from handlers.p_handler import register_p
from handlers.fr_handler import register_fr
from handlers.whale_handler import register_whale

from keep_alive import keep_alive

# ✅ Logging ayarları
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)  # ✅ DOĞRU (alt tireli)

# ✅ .env yükleme
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN bulunamadı! Render Environment veya .env kontrol et.")

def main():
    keep_alive()

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Komut kayıtları
    register_io(application)
    register_nls(application)
    register_npr(application)
    register_etf(application)
    register_ap(application)
    register_price(application)
    register_p(application)
    register_fr(application)
    register_whale(application)

    logger.info("✅ Bot başladı ve polling modunda çalışıyor...")
    application.run_polling()


if __name__ == "__main__":
    main()