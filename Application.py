import requests
from dotenv import load_dotenv
import os
from src.Fetcher import Fetcher

load_dotenv()
API_KEY = os.getenv('API_KEY')


url = "https://api.themoviedb.org/3/trending/all/day?language=en-US"
# url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

class Movie(Fetcher):
    def __init__(self):
        super().__init__(url, headers)
        
    def data(self):
        self.data = self.fetch()
        return self.data

m = Movie()
data = m.data()

print(data['results'])