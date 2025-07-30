import json
import os
import random
import string
from datetime import datetime, timedelta

class URLShortener:
    def __init__(self, filepath='data/urls.json'):
        self.filepath = filepath
        self.urls = {}
        self.load_urls()

    def load_urls(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    self.urls = json.load(f)
                except json.JSONDecodeError:
                    self.urls = {}

    def save_urls(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.urls, f, indent=4)

    def generate_shortcode(self, length=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def shorten(self, original_url, days_valid=7):
        if not original_url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL format.")
        shortcode = self.generate_shortcode()
        while shortcode in self.urls:
            shortcode = self.generate_shortcode()

        expiry = (datetime.now() + timedelta(days=days_valid)).isoformat()
        self.urls[shortcode] = {'url': original_url, 'expiry': expiry}
        self.save_urls()
        return shortcode

    def redirect(self, shortcode):
        if shortcode not in self.urls:
            raise KeyError("Shortcode not found.")
        if datetime.now() > datetime.fromisoformat(self.urls[shortcode]['expiry']):
            raise Exception("Shortcode expired.")
        return self.urls[shortcode]['url']

    def delete(self, shortcode):
        if shortcode in self.urls:
            del self.urls[shortcode]
            self.save_urls()
            return True
        return False

    def list_urls(self):
        return self.urls

    def expired_urls(self):
        for code, data in self.urls.items():
            if datetime.now() > datetime.fromisoformat(data['expiry']):
                yield code
