from environs import Env
#
# # ADMINS=835792297
# # BOT_TOKEN="5712717261:AAFVji0TUkHDKpVtQJLl2ocjXkgD-xtwqN8"
# #private
# # IS_POSTING_REQUESTED=False
# # environs kutubxonasidan foydalanish
env = Env()
env.read_env()


# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
# import os
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = str(os.environ.get("BOT_TOKEN")) # Bot toekn
# ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
# IP = str(os.environ.get("ip"))  # Xosting ip manzili