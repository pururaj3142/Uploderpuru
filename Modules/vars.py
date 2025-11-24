#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22049628"))
API_HASH = environ.get("API_HASH", "db9c4ee4be741f296522a9bb9a945722")
BOT_TOKEN = environ.get("BOT_TOKEN", "7615038215:AAHa3O-tVEfZHE_1p9sD0kLpIPVGEryTgD8")

OWNER = int(environ.get("OWNER", "670897324"))
CREDIT = environ.get("CREDIT", "DP 𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '670897324').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '670897324').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

