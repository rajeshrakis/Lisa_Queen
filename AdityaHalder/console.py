import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")

#-----------------------------------------------------------------------------------------------
# Aishu
#API_ID = int(getenv("API_ID", "8045459"))
#API_HASH = getenv("API_HASH", "e6d1f09120e17a4372fe022dde88511b")
#BOT_TOKEN = getenv("BOT_TOKEN", "7068876137:AAEO6UXBfVcj9BMPXsbdAgApCntlXmYjNTw")
#STRING_SESSION = getenv("STRING_SESSION", "BQDMBnkAYiOVd1XgRlwY7fGlRrmYnn79K2KzLfsXiVAFVRYYfmTzSslg4VMO9zi3V-8UvChSAZJiu4OFnNCHnFYKstELWLGKF4KW70ml64zlF8mgCnAtUPDvJXpJtgrIcjZr-ieZAgda99Giv_ivVbh2V5wLqgSYUbSZ_GKGM4usnJvQFZg6YGMoTMWKQPuZhxphI74-_PyXED5xHpoYpBjbaw00wy8RKJzw3e_NMpXwID5Io1P2uBlx9vbmLcJMHO7DK4YvwsCXQUBNhskfzSiWQqpcVH_eZEW2NN-1uWKDsWbVZPY4PDjraaBVhF5rOi_MVx4oBTAzCV1hT2BGsljeQb7AAAAAEyRzmXAA")
#MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://zewdatabase:ijoXgdmQ0NCyg9DO@zewgame.urb3i.mongodb.net/ontap?retryWrites=true&w=majority")
#LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002063555777"))

# Rajesh
API_ID = int(getenv("API_ID", "13371001"))
API_HASH = getenv("API_HASH", "f9e4a79850af44c26d736453a95308fc")
BOT_TOKEN = getenv("BOT_TOKEN", "6773882212:AAGxTyLGiKX-8syKmtgRbHD4Jn5NTiem0DA")
STRING_SESSION = getenv("STRING_SESSION", "BQB6w5MAqoqMLOuUiivDmxzkNQA01seula8MBuWfkeby9xM5h7MrEA6-nc3f2TzNIepXE1vK_nMST04Sv_oQyzlYNobJ9rLJ65Ug_RoliF7msVzU8_6fweL-P10Dh05Tjs9gk_m-uqvW_xu_LJGAi4DwIAe0d0j0ZV9cNs57yS136aUuu2RlTdoQLR0KNTpi2hSvWJccQylC3yci_nMUqQ4eIpohiunKi8optfAw1eA96FyS-Oyejf3VW7n3YF1mj7v2zAcU7tN4yeVj7zphGn8T7wNc6Fihe8t6KY-JCFyhG_EX7Nbt1sBDY74EWlYsn1Ux86xdwTfcFQ3Dvuavp1TdIPQf1QAAAABMXtJJAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002063555777"))


# Book_Villain
#API_ID = int(getenv("API_ID", "29650844"))
#API_HASH = getenv("API_HASH", "6154d581d370cbdadd240292c456d7a2")
#BOT_TOKEN = getenv("BOT_TOKEN", "7296460979:AAHzGWipkdUIxU6WUYT4hbGqGcK8S6pSqA8")
#STRING_SESSION = getenv("STRING_SESSION", "BQHEb5wADIXYxwyyPRWHkmVI-aldtLm44cjCdjqzooPdyoquoRaK6HRx1f03Kas09zqXHHZeFeyFSOsqTZA2CMd_2EwblUuU2cd_EV1DeLZnznILN91Mm7N7BCE7QU5FQKZqKuUbBUtAVU418XstovD7dtjRbq4c6YTRz9v5NftM8RUaPdMiix08SoSDPLTMtoVhwW4mONLSOt4drT2OSh1ZEF6h0eOKTfbb2bfSpk-rtCiJsNq8qL_XomIDJKb9LYRZ-m6L_rpd2HKeOz4IFKmuBVrJzSlimmFHzWGMK3mbObaDewK5CQExmtqiBE5GfPFbFH2C1ukjTEEF04BEdvZZ0UontgAAAABEKZxZAA")
#MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")
#LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002063555777"))


# Demon_Queen
#API_ID = int(getenv("API_ID", "20883765"))
#API_HASH = getenv("API_HASH", "8fe7c465d01b1bee8c2156143654ecd1")
#BOT_TOKEN = getenv("BOT_TOKEN", "7003201598:AAHAkwHYDgHTZgftpPej_ep2CgLXSTIMZaw")
#STRING_SESSION = getenv("STRING_SESSION", "BQE-qTUAqDzOvMtdXsq3Fjzjx9mpVtAVxhD5Qj5G7YvQhZATknZBp2NceRdl_7NkYyLw-B2spiTn47O46vINlYBia7KeY9mwUn8qSbtVXE3kFA4yRQ70WaQPcEiaqzla3KHwVwPbFOfR10xwiRsUl9TDd4zXaj1ld4BYVkyWOSmo_vidjPCo1icviFVAzE1_Y8Erm5hImUokK9QYttckGbmuMwJgp7huJiauowPJot06gMfHg5Vm9QTcWFLvLdoZhMAHzqGEmIODGwWwbq0TFILife610fX5q1ee4dzuU3B-dvnzRLoG9TWedSZsA8DI-2ATleEOEqZrr8xKKL0eq0itv7IXcAAAAAGgWO11AA")
#MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://admin:pass@cluster0.bqss1.mongodb.net/todo?retryWrites=true&w=majority")
#LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002063555777"))

# Lisa_Queen
#API_ID = int(getenv("API_ID", "22431483"))
#API_HASH = getenv("API_HASH", "081facce8bed58c074ede1ab5b0c523c")
#BOT_TOKEN = getenv("BOT_TOKEN", "7411947176:AAGVNuQsKSBQ0ZECQ73nPg0F2ltpk3szzdI")
#STRING_SESSION = getenv("STRING_SESSION", "BQFWRvsAlV6jO9pEWKi-Apz0eb7r-ZyuJHaQ-m8JiFVx7aZF7zauN_05-yHIvEJovd7o7Ph3Qnja8dhq4IQqEJLn08XSlfj0Gd_G_L5m4DarecsN2_bSAcu3cjmLbTDtFouROX2uyMlpe0f9bNW0UFxi7MYWEeGngBK6IYXqWtwFGQEYTMiNj1o_0HMulaQxXwpB83SIfXR4yJhKxfe9j7eAjmO7HvqNdlZhappf-nqdlVwf0RiuY3v53OBYLJvNaez3-dt00XyZkXhSxbgfJblR-Wr98qmt8VzFGPVSMm_n2ATof5s5kiryMY5-4CCgR75H52NoGastphCiIoXpWgV70RBQAAAAE9MQ-rAA")
#MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://admin:pass@cluster0.bqss1.mongodb.net/todo?retryWrites=true&w=majority")
#LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002063555777"))

#------------------------------------------------------------------------------------------------------------------------------

# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\nʜᴇʏ ɪ'ᴍ 𝐇𝐞𝐚𝐫𝐭𝐁𝐞𝐚𝐭-✗-𝐁𝐨𝐭\n\n☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\n➽─────────────────❥\n\n💕 ᴛᴀɢ ᴍʏ ʟᴏᴠᴇ 🦋\n https://t.me/HeartBeat_Muzic \n\n➽─────────────────❥\n\n😈 ᴏᴛʜᴇʀᴡɪꜱᴇ, ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ʙᴏꜱꜱ ᴄᴏᴍᴇꜱ, ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ᴍᴇ..\nʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏʙʟᴏᴄᴋ (ᴜᴘᴛᴏ 3 ᴍᴇꜱꜱᴀɢᴇꜱ)\n\n**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 3))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/9ee37cccd7bf55c3ec953.png")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Genius")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

