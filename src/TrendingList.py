import os
import requests
from dotenv import load_dotenv
from Fetcher import Fetcher
from rich import print

load_dotenv()
API_KEY = os.getenv('API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

class TrendingList(Fetcher):
    def __init__(self, url):
        self.url = url
        super().__init__(self.url, headers=headers)
        tw = self.time_window()
        self.base_url = f'{url}/{tw}'

    def time_window(self):
        while True:
            user_choice = input('Enter the time window for the list (d for day, w for week): ').lower()
            
            if user_choice == 'd':
                return 'day'
            elif user_choice == 'w':
                return 'week'
            else:
                print('[red]Wrong Input!![/red]')
        
    def data(self):
        self.data = self.fetch()
        return self.data

    def show_list(self, result_data):
        self.result_data = result_data

        for index, movies in enumerate(self.result_data):
            if "name" in self.result_data[index]:
                print(f"{index+1}: {self.result_data[index]['name']}")
            elif "title" in self.result_data[index]:
                print(f"{index+1}: {self.result_data[index]['title']}")
            else:
                print("[red]Something went wrong[/red]")
                
    