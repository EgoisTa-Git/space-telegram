import os
import time

import telegram
import requests
from urllib import parse
from dotenv import load_dotenv

from fetch_spacex import get_spacex_images
from fetch_nasa import get_apod_images, get_epic_images


def save_images(image_dir=, images):
    for image_url in images:
        url_parse = parse.urlparse(image_url)
        image_name = os.path.basename(url_parse.path)
        with open(f'{image_dir}/{image_name}', 'wb') as file:
            file.write(requests.get(image_url).content)


if __name__ == '__main__':
    load_dotenv()
    spacex_url = 'https://api.spacexdata.com/v5/launches' \
                 '/5eb87d42ffd86e000604b384'
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    epic_url = 'https://api.nasa.gov/EPIC'
    nasa_api_key = os.getenv('NASA_API')
    tg_api_key = os.getenv('TG_API')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    post_delay = os.getenv('POST_DELAY_IN_SECONDS')
    amount_of_apods = 5
    amount_of_epics = 2
    dir_name = 'images'
    try:
        os.makedirs(dir_name)
    except FileExistsError:
        pass
    save_images(
        dir_name,
        get_spacex_images(spacex_url),
    )
    save_images(
        dir_name,
        get_apod_images(nasa_api_key, nasa_url, amount_of_apods),
    )
    save_images(
        dir_name,
        get_epic_images(nasa_api_key, epic_url, amount_of_epics),
    )
    # bot = telegram.Bot(token=tg_api_key)
    # bot.send_message(chat_id=tg_chat_id, text='Hi to all subscribers!')
    # images_to_send = (file for file in os.listdir(dir_name))
    # while True:
    #     try:
    #         image_name_to_send = next(images_to_send)
    #         with open(f'{dir_name}/{image_name_to_send}',
    #                   'rb') as image_to_send:
    #             bot.send_photo(chat_id=chat_id, photo=image_to_send)
    #         time.sleep(float(post_delay))
    #     except StopIteration:
    #         print('Больше новый файлов нет')
    #         break
