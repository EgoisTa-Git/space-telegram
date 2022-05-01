import os
import random
import time
from pathlib import Path

import telegram
import requests
from urllib import parse
from dotenv import load_dotenv

from fetch_spacex import get_spacex_images, spacex_url
from fetch_nasa import get_apod_images, get_epic_images, nasa_url, epic_url

DIR_NAME = 'images'


def save_images(image_dir, images):
    for image_url in images:
        url_parse = parse.urlparse(image_url)
        image_name = os.path.basename(url_parse.path)
        with open(f'{image_dir}/{image_name}', 'wb') as file:
            file.write(requests.get(image_url).content)


if __name__ == '__main__':
    load_dotenv()
    tg_api_key = os.getenv('TG_API')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    post_delay = float(os.getenv('POST_DELAY_IN_SECONDS'))
    amount_of_apods = 5
    amount_of_epics = 1
    Path(f'{DIR_NAME}').mkdir(parents=True, exist_ok=True)
    save_images(
        DIR_NAME,
        get_spacex_images(spacex_url),
    )
    save_images(
        DIR_NAME,
        get_apod_images(nasa_url, amount_of_apods),
    )
    save_images(
        DIR_NAME,
        get_epic_images(epic_url, amount_of_epics),
    )
    shuffled_images = os.listdir(DIR_NAME)
    random.shuffle(shuffled_images)
    bot = telegram.Bot(token=tg_api_key)
    for image in shuffled_images:
        with open(f'{DIR_NAME}/{image}', 'rb') as image_to_send:
            bot.send_photo(chat_id=tg_chat_id, photo=image_to_send)
        time.sleep(post_delay)
