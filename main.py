# ======================================
# ✅ MegaBot Final - main.py
# Ana bot başlatma, handler kayıtları, JobQueue görevleri
# ======================================

import logging
import datetime
from telegram.ext import ApplicationBuilder

from handlers.io_handler import register_io
from handlers.nls_handler import register_nls
from handlers.npr_handler import register_npr
from handlers.eft_handler import register_eft
from handlers.ap_handler import register_ap
from handlers.price_handler import register_price
from handlers.p_handler import register_p
from handlers.fr_handler import register_fr
from handlers.whale_handler import register_whale

from keep_alive import keep_alive

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    keep_alive()  # Render Free ping sistemi

    application = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

    # Komut kayıtları
    register_io(application)
    register_nls(application)
    register_npr(application)
    register_eft(application)
    register_ap(application)
    register_price(application)
    register_p(application)
    register_fr(application)
    register_whale(application)

    logger.info("Bot başladı.")

    application.run_polling()


if __name__ == "__main__":
    main()
