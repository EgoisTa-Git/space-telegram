import datetime

import requests

nasa_url = 'https://api.nasa.gov/planetary/apod'
epic_url = 'https://api.nasa.gov/EPIC'


def get_apod_images(api_key, url=nasa_url, amount=1):
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


def get_epic_images(api_key, url=epic_url, amount=1):
    epic_images = []
    path_to_api = '/api/natural'
    payload = {
        'api_key': api_key,
    }
    data_response = requests.get(f'{url}{path_to_api}', params=payload)
    data_response.raise_for_status()
    for number in range(amount):
        date = data_response.json()[number]['date']
        date = datetime.datetime.fromisoformat(date).strftime('%Y/%m/%d')
        image_name = data_response.json()[number]['image']
        path_to_archive = f'/archive/natural/{date}/png/{image_name}.png'
        response = requests.get(f'{url}{path_to_archive}', params=payload)
        response.raise_for_status()
        epic_images.append(response.url)
    return epic_images
