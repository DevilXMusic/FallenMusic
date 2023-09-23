from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/fa6e6d1558e6539723b6d.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2f60cde5308dc2836cd9b.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Mission_Successs")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/About_Info_Devil")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://telegra.ph/file/34de57f748fccecebacc3.jpg"
