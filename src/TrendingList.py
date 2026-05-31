import os
import time 
import random
import requests
import pyfiglet
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
            user_choice = input('\nEnter the time window for the list (d for day, w for week): ').lower()
            
            if user_choice == 'd':
                return 'day'
            elif user_choice == 'w':
                return 'week'
            else:
                print('[red]Wrong Input!![/red]')
        
    def data(self):
        self.data = self.fetch()
        return self.data

    def show_list(self, list_count, result_data):
        self.result_data = result_data
        self.list_count = list_count

        self.banner_text = f'\nTop {list_count} Trending\n'
        self.colors = ["red", "green", "blue", "magenta", "cyan", "bright_red", "bright_green", "bright_blue", "bright_cyan", "navy_blue", "cyan2", "spring_green1", "purple4", "grey50"]

        print(pyfiglet.figlet_format(self.banner_text, font="slant"))

        for index, movies in enumerate(self.result_data):
            if list_count < (index + 1):
                break
            else:
                self.color = random.randint(0, len(self.colors) - 1)

                if "name" in self.result_data[index]:
                    print(f"{index+1}: [{self.colors[self.color]}]{self.result_data[index]['name']}[/{self.colors[self.color]}]")
                elif "title" in self.result_data[index]:
                    print(f"{index+1}: [{self.colors[self.color]}]{self.result_data[index]['title']}[/{self.colors[self.color]}]")
                else:
                    print("[red]Something went wrong[/red]")
        time.sleep(1)
                
    