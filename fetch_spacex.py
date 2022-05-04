import requests

from save_files import save_images

SPACEX_URL = 'https://api.spacexdata.com/v5/launches'


def get_spacex_images(target_url=SPACEX_URL):
    response = requests.get(target_url)
    response.raise_for_status()
    for launch in response.json()[::-1]:
        if launch['links']['flickr']['original']:
            return launch['links']['flickr']['original']


if __name__ == '__main__':
    save_images(get_spacex_images())
