import os
import random
import time

import telegram
from dotenv import load_dotenv

from save_files import DIR_NAME

if __name__ == '__main__':
    load_dotenv()
    tg_api_key = os.getenv('TG_API')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    post_delay = float(os.getenv('POST_DELAY_IN_SECONDS'))
    shuffled_images = os.listdir(DIR_NAME)
    random.shuffle(shuffled_images)
    bot = telegram.Bot(token=tg_api_key)
    for image in shuffled_images:
        with open(f'{DIR_NAME}/{image}', 'rb') as image_to_send:
            bot.send_photo(chat_id=tg_chat_id, photo=image_to_send)
        time.sleep(post_delay)
