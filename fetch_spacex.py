import requests


def get_spacex_images(target_url):
    response = requests.get(target_url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']
