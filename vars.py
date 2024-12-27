import os

API_ID    = os.environ.get("API_ID", "4942197")
API_HASH  = os.environ.get("API_HASH", "13248a2c551b73193969b42194023635")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7342369117:AAERxlLiwFYmuPBdiO8Hnp9-7BuoOLWIlC4") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
