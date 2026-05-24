import requests
from rich import print

class Fetcher:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def fetch(self):
        r = requests.get(self.base_url, headers=self.headers)
        if r.status_code == 200:
            return r 
        else:
            r.raise_for_status()
