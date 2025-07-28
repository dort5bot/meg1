# ======================================
# ✅ MegaBot Final - handlers/apikey_handler.py
# /apikey komutu - API key ekleme, güncelleme, silme (kullanıcı bazlı)
# ======================================
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.csv_utils import save_apikey, delete_apikey

async def apikey_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Kullanım:\n/apikey [API_KEY] [SECRET]\n/apikey sil")
        return

    if context.args[0].lower() == "sil":
        delete_apikey(update.effective_user.id)
        await update.message.reply_text("🗑 API key silindi.")
    else:
        if len(context.args) < 2:
            await update.message.reply_text("⚠️ API Key ve Secret girin.")
            return
        save_apikey(update.effective_user.id, context.args[0], context.args[1])
        await update.message.reply_text("✅ API key kaydedildi.")

def register_apikey_handlers(app):
    app.add_handler(CommandHandler("apikey", apikey_command))
