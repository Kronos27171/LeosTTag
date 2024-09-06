import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "20416838"))
API_HASH = getenv("API_HASH", "c393e906f7d2610ad5322af34ee4197d")
BOT_TOKEN = getenv("BOT_TOKEN", "7547386899:AAG0X5On0pSq8HBFoq6cRko7NsBdYp1aN2g")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hakoqq27:Hakan2717@cluster0.qpyasii.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001795728747"))
OWNER_ID = int(getenv("OWNER_ID", 6939182031))
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Kronos27171/LeosTTag",
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/o1GaddaR")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/o1GaddaR")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
STRING1 = getenv("STRING_SESSION", "BAB-H6UQ7RlUj6GT3MzoP1NkwsMUm7LvUmTXfPe6uH5i7mnrtEaR1hR0hwVqa8lTgjm2JUrjP8tk3RLUZ3XdhCnsP6NxpyX4T8pABnglgHyi2kxkdLuPHL5-PnsiarQWaXqh7QccMU4M3NF7hdxOmTjiO2lgMu9z2f9XusMZZdqF79lTGf5cfoyiupI3EtvxVz3Wf8JpV_-e_DdJRmN_hlpoqXVSLCU09v-OwyAqyzzEYfawtfFv9ycwDxCR3i1w9YHr5Z8eMEu1uyu61RxN44636sUEg2ivBBDjK7PiVkto5DBx2ZgIlvy-2578max8F6Kj74bD1-rDcB9iTBuT4e5cAAAAAZ2bg88A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/f7912b86c79b736c2e5bf.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/3d5424b7f19a6f2e41e85.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/7ad11d3ef1687cbb79651.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
