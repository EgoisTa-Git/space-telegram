import datetime
import os

import requests
from dotenv import load_dotenv

from save_files import save_images

NASA_URL = 'https://api.nasa.gov/planetary/apod'
EPIC_URL = 'https://api.nasa.gov/EPIC'


def get_apod_urls(api_key, amount=1):
    payload = {
        'api_key': api_key,
        'count': amount,
    }
    response = requests.get(NASA_URL, params=payload)
    response.raise_for_status()
    apods = response.json()
    apod_urls = []
    for apod in apods:
        if apod['media_type'] == 'image':
            apod_urls.append(apod['url'])
    return apod_urls


def get_epic_image_urls(api_key, amount=1):
    epic_image_urls = []
    path_to_api = '/api/natural'
    payload = {
        'api_key': api_key,
    }
    data_response = requests.get(f'{EPIC_URL}{path_to_api}', params=payload)
    data_response.raise_for_status()
    for number in range(amount):
        date = data_response.json()[number]['date']
        date = datetime.datetime.fromisoformat(date).strftime('%Y/%m/%d')
        image_name = data_response.json()[number]['image']
        path_to_archive = f'/archive/natural/{date}/png/{image_name}.png'
        response = requests.get(f'{EPIC_URL}{path_to_archive}', params=payload)
        response.raise_for_status()
        epic_image_urls.append(response.url)
    return epic_image_urls


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API')
    amount_of_apods = 5
    amount_of_epics = 1
    save_images(get_apod_urls(nasa_api_key, amount_of_apods))
    save_images(get_epic_image_urls(nasa_api_key, amount_of_epics))
