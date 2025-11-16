import telebot, time
from telebot.types import InputMediaAnimation

TOKEN = "ТОКЕН"
POST_LINK = "https://t.me/bfmc_rus/1"
GIF_PATH = "IMG_1490.MP4"

bot = telebot.TeleBot(TOKEN)

groups = open("groups_ru.txt").read().splitlines()

def send_post():
    for group in groups:
        try:
            with open(GIF_PATH, 'rb') as gif:
                bot.send_animation(group,gif,caption=POST_LINK)
        except:
            pass
        time.sleep(1)

while True:
    send_post()
    time.sleep(600)
``` |
| **4** | **Commit** |
| **5** | Добавь `groups_ru.txt` (вставь 100+ групп) |
| **6** | Добавь `gif.gif` |
| **7** | Добавь `requirements.txt`:  
