# ======================================
# ✅ MegaBot Final - utils/csv_utils.py
# CSV okuma/yazma, favori listesi, Funding Rate & Whale kayıtları, API key yönetimi
# ======================================
import csv, json, os

DATA_DIR = "data"
FAV_FILE = os.path.join(DATA_DIR, "fav_list.json")
APIKEY_FILE = os.path.join(DATA_DIR, "apikeys.json")

# ---------------- Favori coin listesi ----------------
def _load_json(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_favorite(user_id, coins):
    favs = _load_json(FAV_FILE)
    favs[str(user_id)] = list(set(favs.get(str(user_id), []) + coins))
    _save_json(FAV_FILE, favs)

def remove_favorite(user_id, coins):
    favs = _load_json(FAV_FILE)
    favs[str(user_id)] = [c for c in favs.get(str(user_id), []) if c not in coins]
    _save_json(FAV_FILE, favs)

def list_favorites(user_id):
    return _load_json(FAV_FILE).get(str(user_id), [])

# ---------------- API key yönetimi ----------------
def save_apikey(user_id, api_key, secret):
    keys = _load_json(APIKEY_FILE)
    keys[str(user_id)] = {"api_key": api_key, "secret": secret}
    _save_json(APIKEY_FILE, keys)

def delete_apikey(user_id):
    keys = _load_json(APIKEY_FILE)
    if str(user_id) in keys:
        del keys[str(user_id)]
        _save_json(APIKEY_FILE, keys)

def get_apikey(user_id):
    return _load_json(APIKEY_FILE).get(str(user_id), {})

# ---------------- CSV kayıt örneği ----------------
def append_csv(file, row, max_rows=60):
    rows = []
    if os.path.exists(file):
        with open(file, "r", newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
    rows.append(row)
    if len(rows) > max_rows:
        rows = rows[-max_rows:]
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
