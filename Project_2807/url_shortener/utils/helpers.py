import re

def is_valid_url(url):
    return re.match(r'^https?://[^\s]+$', url)
