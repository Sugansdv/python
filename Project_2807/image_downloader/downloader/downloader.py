import os
import requests
from PIL import Image
from io import BytesIO

class ImageDownloader:
    def __init__(self, urls, save_dir="images"):
        self.urls = urls
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def download_all(self):
        for i, url in enumerate(self.urls):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
                ext = img.format.lower()
                filename = os.path.join(self.save_dir, f"image_{i+1}.{ext}")
                img.save(filename)
                yield f"✅ Downloaded {filename}"
            except Exception as e:
                yield f"❌ Failed to download from {url}: {e}"
