import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28766774'))
API_HASH = environ.get('API_HASH', 'b8b7a890c64bca1621f3e5666dbd0894')
BOT_TOKEN = environ.get('BOT_TOKEN', '6673366631:AAELGj2QIeoIdUuDbEXqR2i1FeedvxpxLEM')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', 'True'))
PICS = environ.get('PICS', 'https://telegra.ph/file/165723fe0fcaf9f7c054d.jpg https://telegra.ph/file/4aa5168563cf80b429c82.jpg https://telegra.ph/file/bedb7372c81593ae4d035.jpg https://telegra.ph/file/28f538620997fee258331.jpg https://telegra.ph/file/aa8dcd7bdd08b71adea9b.jpg https://telegra.ph/file/0687ce09d40b00e378ce3.jpg').split()  # Replace '...' with your image URLs

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1124414278').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1124414278').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1001915221697'))
AUTH_GROUPS = [int(ch) for ch in environ.get('AUTH_GROUP', '-1001861725083').split()] if environ.get('AUTH_GROUP') else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://Sujansg:YEl29iSyxtAKNZT1@cluster0.p0ng9ea.mongodb.net/?retryWrites=true&w=majority')
DATABASE_NAME = environ.get('DATABASE_NAME', 'All Movie At One')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001856149007'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '-1001818864710')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', 'False'), False)
IMDB = is_enabled(environ.get('IMDB', 'True'), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', 'True'), False)
CUSTOM_FILE_CAPTION = environ.get('CUSTOM_FILE_CAPTION', "Your custom caption here")
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', "Your IMDb template here")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get('LONG_IMDB_DESCRIPTION', 'False'), False)
SPELL_CHECK_REPLY = is_enabled(environ.get('SPELL_CHECK_REPLY', 'True'), False)
MAX_LIST_ELM = environ.get('MAX_LIST_ELM', None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', '-1001856149007'))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1001935596221').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', 'True'), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', 'True'), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', 'True'), False)

# LazyRenamer Configs
FLOOD = int(environ.get('FLOOD', '10'))
LAZY_MODE = bool(environ.get('LAZY_MODE'))
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '1124414278').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else []
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', '-1001830309583'))

# AI
OPENAI_API = environ.get('OPENAI_API', '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')
AI = is_enabled(environ.get('AI', 'True'), False)
LAZY_AI_LOGS = int(environ.get('LAZY_AI_LOGS', '-1001913444688'))

# Requested Content template variables
ADMIN_USRNM = environ.get('ADMIN_USRNM', 'Harsha_S_G')
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM', 'filmzoneadd0')
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM', '')
LAZY_YT_HANDLE = environ.get('LAZY_YT_HANDLE', '@Ultimately-YT09')
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', '-1001861725083')

# URL Shortener
URL_MODE = is_enabled(environ.get('URL_MODE', 'True'), False)
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'tnshort.net')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '2eb38117e76c51df0762f15001bdd6acd9c19053')
LZURL_PRIME_USERS = [int(lazyurlers) if id_pattern.search(lazyurlers) else lazyurlers for lazyurlers in environ.get('LZURL_PRIME_USERS', '5965340120').split()]
lazy_groups = environ.get('LAZY_GROUPS', '-1001861725083')
LAZY_GROUPS = [int(lazy_groups) for lazy_groups in lazy_groups.split()] if lazy_groups else None
my_users = [int(my_users) if id_pattern.search(my_users) else my_users for my_users in environ.get('MY_USERS', '-1001805224802').split()]
MY_USERS = my_users if my_users else []

# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if (not ON_HEROKU or getenv('FQDN')) else APP_NAME

