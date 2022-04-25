import datetime
import os

import telegram
import requests
from urllib import parse
from dotenv import load_dotenv


def save_image(image_dir, image_url):
    url_parse = parse.urlparse(image_url)
    image_name = os.path.basename(url_parse.path)
    with open(f'{image_dir}/{image_name}', 'wb') as file:
        file.write(requests.get(image_url).content)


def get_spacex_images(target_url):
    response = requests.get(target_url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_apod_images(api_key, url, amount):
    payload = {
        'api_key': api_key,
        'count': amount,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    apods = response.json()
    apod_images = []
    for apod in apods:
        if apod['media_type'] == 'image':
            apod_images.append(apod['url'])
    return apod_images


def get_epic_images(api_key, url, amount):
    path_to_api = '/api/natural'
    payload = {
        'api_key': api_key,
    }
    data_response = requests.get(url+path_to_api, params=payload)
    data_response.raise_for_status()
    date = data_response.json()[amount]['date']
    date = datetime.datetime.fromisoformat(date).strftime('/%Y/%m/%d')
    image_name = data_response.json()[amount]['image']
    path_to_archive = '/archive/natural' + date + '/png/' + image_name + '.png'
    response = requests.get(url+path_to_archive, params=payload)
    response.raise_for_status()
    return response.url


if __name__ == '__main__':
    load_dotenv()
    spacex_url = 'https://api.spacexdata.com/v5/launches' \
                 '/5eb87d42ffd86e000604b384'
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    epic_url = 'https://api.nasa.gov/EPIC'
    nasa_api_key = os.getenv('NASA_API')
    tg_api_key = os.getenv('TG_API')
    chat_id = '@apodvsepic'
    amount_of_apods = 30
    amount_of_epics = 5
    dir_name = 'images'
    try:
        os.makedirs(dir_name)
    except FileExistsError:
        pass
    # spacex_images = get_spacex_images(spacex_url)
    # for image in spacex_images:
    #     save_image(dir_name, image)
    # apod_images = get_apod_images(
    #     nasa_api_key,
    #     nasa_url,
    #     amount_of_apods,
    # )
    # for image in apod_images:
    #     save_image(dir_name, image)
    # for count in range(amount_of_epics):
    #     epic_image = get_epic_images(
    #         nasa_api_key,
    #         epic_url,
    #         count,
    #     )
    #     save_image(dir_name, epic_image)
    bot = telegram.Bot(token=tg_api_key)
    # print(bot.getMe())
    bot.send_message(chat_id=chat_id, text='Hi to all subscribers!')
