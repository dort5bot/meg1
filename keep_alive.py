# ✅ Render Free ping sistemi
# ======================================
# ✅ MegaBot Final - keep_alive.py
# Render Free ping sistemi (botun uyumasını önler)
# ======================================
from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "MegaBot is alive!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()
