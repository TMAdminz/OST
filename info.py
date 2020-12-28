import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ['AUTH_USERS'].split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
<i>I am </i><b>@TM_Spotifybot.</b> <i>Ask me what song you want with the <u><b>correct name.</b></u> Ask using <u><b>Inline Mode.</b></u></i>

<b><i>Join Our Channels:©

</i>1. <a href='https://telegram.dog/TM_OST'>TM_OST</a>  |  <a href='https://telegram.dog/joinchat/RedFUkR_eDejR8A8'>Join Discussion Group</a>

2. <a href='https://telegram.dog/joinchat/UqWn1JwDclHQSzoM'>TM_OST - Private Channel</a></b>
"""

SHARE_BUTTON_TEXT = "<i>I am </i><b>@TM_Spotifybot.</b> <i>Ask me what song you want with the <u><b>correct name.</b></u> Ask using <u><b>Inline Mode.</b></u></i>\n<b><i>Join Our Channels:©\n</i>1. <a href='https://telegram.dog/TM_OST'>TM_OST</a>  |  <a href='https://telegram.dog/joinchat/RedFUkR_eDejR8A8'>Join Discussion Group</a>\n2. <a href='https://telegram.dog/joinchat/UqWn1JwDclHQSzoM'>TM_OST - Private Channel</a></b>"
