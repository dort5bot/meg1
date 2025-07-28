# ✅ Ana bot başlatma, handler kayıtları, JobQueue görevleri
# ======================================
# ✅ MegaBot Final - main.py
# Ana bot başlatma, handler kayıtları, JobQueue görevleri
# ======================================
import logging
from telegram.ext import ApplicationBuilder
from keep_alive import keep_alive
from handlers.io_handler import register_io_handlers
from handlers.nls_handler import register_nls_handlers
from handlers.npr_handler import register_npr_handlers
from handlers.eft_handler import register_eft_handlers
from handlers.ap_handler import register_ap_handlers
from handlers.price_handler import register_price_handlers
from handlers.p_handler import register_p_handlers
from handlers.fr_handler import register_fr_handlers
from handlers.whale_handler import register_whale_handlers
from handlers.apikey_handler import register_apikey_handlers
import os

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ✅ .env'den token çek
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env dosyasında tanımlı değil!")

# ✅ Uygulama başlat
app = ApplicationBuilder().token(BOT_TOKEN).build()

# ✅ Handler kayıtları
register_io_handlers(app)
register_nls_handlers(app)
register_npr_handlers(app)
register_eft_handlers(app)
register_ap_handlers(app)
register_price_handlers(app)
register_p_handlers(app)
register_fr_handlers(app)
register_whale_handlers(app)
register_apikey_handlers(app)

# ✅ Render Free'de botun uyumaması için keep_alive
keep_alive()

logger.info("✅ MegaBot başlatılıyor...")
app.run_polling()
