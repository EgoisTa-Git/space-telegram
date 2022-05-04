import os
from pathlib import Path

import requests
from urllib.parse import urlparse

DIR_NAME = 'images'


def save_images(images, image_dir=DIR_NAME):
    Path(f'{DIR_NAME}').mkdir(parents=True, exist_ok=True)
    for image_url in images:
        url_parse = urlparse(image_url)
        image_name = os.path.basename(url_parse.path)
        with open(f'{image_dir}/{image_name}', 'wb') as file:
            file.write(requests.get(image_url).content)
