"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


import os
import re
import sys
import heroku3
import subprocess
from dotenv import load_dotenv
try:
    from yt_dlp import YoutubeDL
except ModuleNotFoundError:
    file=os.path.abspath("requirements.txt")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file, '--upgrade'])
    os.execl(sys.executable, sys.executable, *sys.argv)

load_dotenv()

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "http://peridot.streamguys.com:7150/Mirchi")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM



class Config:

    # Mendatory Variables
    ADMIN = os.environ.get("AUTH_USERS", "1471469091")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    ADMINS.append(1471469091)
    API_ID = int(os.environ.get("API_ID", "19408128"))
    API_HASH = os.environ.get("API_HASH", "5435067066:AAHdA5Ocszel5O1VpipIBN2WydWd8t7OLwQ")
    CHAT_ID = int(os.environ.get("CHAT_ID", "-1001719920984"))
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5435067066:AAHdA5Ocszel5O1VpipIBN2WydWd8t7OLwQ")
    SESSION = os.environ.get("SESSION_STRING", "BQCiJ7PWJLULSP9lXWpKse0JvITDk9sxqb5DyjWuKBXj2bK68VTwqE-ddpA54VyHiQv5zS5768EI-gBenMut-ecmPMX7RAy2rVQ71fiD531TB-4suWWYi_MM_SWff0R-4sTFokIqtPg3l-eWURrFWdIskhaa3FPZn21iyqt0i2W68KLH6kOcoHTilfl9mJVIqx9jE78yNdewKLV6IqNnzLQ8dNZc9dVWNqv2HyT3Kxinh-uJusSrxCY3Na-1ikn85WYjjk0hexN9L5pGxBYv_9viH_BV0SZtV6hn5uMv9-7RQOEi2sID4X_q3Wd3by_Ndx_8pSAZDTBMDtza6GKoVv6KAAAAAUBHgvcA")

    # Optional Variables
    STREAM_URL=finalurl
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001719920984")
    LOG_GROUP = int(LOG_GROUP) if LOG_GROUP else None
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "False")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    REPLY_MESSAGE = REPLY_MESSAGE or None
    DELAY = int(os.environ.get("DELAY", 10))
    EDIT_TITLE=os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "False":
        EDIT_TITLE=None
    RADIO_TITLE=os.environ.get("RADIO_TITLE", "RADIO 24/7 | LIVE")
    if RADIO_TITLE == "False":
        RADIO_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))

    # Extra Variables ( For Heroku )
    API_KEY = os.environ.get("HEROKU_API_KEY", None)
    APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    if not API_KEY or \
       not APP_NAME:
       HEROKU_APP=None
    else:
       HEROKU_APP=heroku3.from_key(API_KEY).apps()[APP_NAME]

    # Temp DB Variables ( Don't Touch )
    msg = {}
    playlist=[]

