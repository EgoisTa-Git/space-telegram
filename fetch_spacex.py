import requests

from save_files import save_images

SPACEX_URL = 'https://api.spacexdata.com/v5/launches' \
                 '/5eb87d42ffd86e000604b384'


def get_spacex_images(target_url=SPACEX_URL):
    response = requests.get(target_url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    save_images(get_spacex_images())
