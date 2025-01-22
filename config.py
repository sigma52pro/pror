import os
from configparser import ConfigParser

config = ConfigParser()
config.read('confug.ini')


#BOT_TOKEN = config.get('bot','token',fallback=os.getenv('BOT_TOKEN'))
BOT_TOKEN = os.getenv(
    'BOT_TOKEN',
    config.get('bot','token',fallback=None)
)
if not BOT_TOKEN:
    exit('Please BOT_TOKEN')
DOG_URL = 'https://masterpiecer-images.s3.yandex.net/9586e0deb07711ee8f9e5e02d8de8a56:upscaled'

DOG_PIC_FILE_ID = 'AgACAgIAAxkDAAIB12d2qsA3r2xUOX2QQYBiqcDdCzNkAALE5zEbbsmwS7dV15ok4ZtvAQADAgADeAADNgQ'

admin_ids = config.get('admin','admin_ids',fallback="")
#print(repr(admin_ids))
admin_ids = [admin_id.strip() for admin_id in admin_ids.split(",")]
#print(repr(admin_ids))
admin_ids =[int(admin_id)
            for admin_id
            in admin_ids
            if admin_id
            ]
#print(repr(admin_ids))
BOT_USER_ADMIN_IDS = admin_ids