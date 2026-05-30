import os
import requests
from dotenv import load_dotenv
from .Fetcher import Fetcher
from rich import print

load_dotenv()
API_KEY = os.getenv('API_KEY')

params = 'language=en-US'

url = 'https://api.themoviedb.org/3/trending/movie/'

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

class TrendingMovies(Fetcher):
    def time_window(self):
        while True:
            user_choice = input('Enter the time window for the list (d for day, w for week): ').lower()
            
            if user_choice == 'd':
                return 'day'
            elif user_choice == 'w':
                return 'week'
            else:
                print('[red]Wrong Input!![/red]')
    
    def __init__(self):
        tw = self.time_window()
        structured_url = f'{url}{tw}'
        super().__init__(structured_url, headers=headers)
        
