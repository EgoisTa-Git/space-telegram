import os
from pathlib import Path

import requests
from urllib.parse import urlparse

DIR_NAME = 'images'


def save_images(images, image_dir=DIR_NAME):
    Path(f'{DIR_NAME}').mkdir(parents=True, exist_ok=True)
    for image_url in images:
        response = requests.get(image_url)
        response.raise_for_status()
        url_parse = urlparse(image_url)
        image_name = os.path.split(url_parse.path)[1]
        with open(f'{image_dir}/{image_name}', 'wb') as file:
            file.write(response.content)
