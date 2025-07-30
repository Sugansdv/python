from downloader.downloader import ImageDownloader

urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/800px-June_odd-eyed-cat.jpg",
    "https://www.python.org/static/community_logos/python-logo.png"
]

downloader = ImageDownloader(urls)

print("\n--- Image Download Progress ---")
for result in downloader.download_all():
    print(result)
