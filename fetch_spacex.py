import requests

spacex_url = 'https://api.spacexdata.com/v5/launches' \
                 '/5eb87d42ffd86e000604b384'


def get_spacex_images(target_url=spacex_url):
    response = requests.get(target_url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']
