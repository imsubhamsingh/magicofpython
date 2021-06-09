import os
import requests
import shutil
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
downloaded_img_path = os.path.join(DOWNLOAD_DIR, '1.jpg')

#data pull
url ="https://imgur.com/gallery/k0xfJ9x"
# r = requests.get(url, stream=True)
# r.raise_for_status()
# with open(downloaded_img_path, 'wb') as f:
#     f.write(r.content)



download_file(url, DOWNLOAD_DIR)