import requests
from rich import print

class Fetcher:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        
    @classmethod
    def with_param(cls, base_url, headers, params):
        instance = cls(base_url, headers)
        instance.params = params
        return instance

    def fetch(self):
        r = requests.get(self.base_url, headers=self.headers)
        if r.status_code == 200:
            return r.json()
        else:
            r.raise_for_status()
