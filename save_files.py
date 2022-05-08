import os
from pathlib import Path

import requests
from urllib.parse import urlparse, unquote

DIR_NAME = 'images'


def save_images(image_urls, image_dir=DIR_NAME):
    Path(f'{DIR_NAME}').mkdir(parents=True, exist_ok=True)
    for image_url in image_urls:
        response = requests.get(image_url)
        response.raise_for_status()
        url_parse = urlparse(image_url)
        image_name = unquote(os.path.basename(url_parse.path))
        with open(f'{image_dir}/{image_name}', 'wb') as file:
            file.write(response.content)
