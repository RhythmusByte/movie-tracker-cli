import os
import requests
from rich import print
from dotenv import load_dotenv
from src.TrendingList import TrendingList

load_dotenv()

API_KEY = os.getenv('API_KEY')

trending_all_url = "https://api.themoviedb.org/3/trending/all"
trending_movies_url = 'https://api.themoviedb.org/3/trending/movie'
trending_tv_url = "https://api.themoviedb.org/3/trending/tv"

banner = """
┌─────────────────────────┐
│    Movie Tracker CLI    │
│ Track • Discover • List │
└─────────────────────────┘
"""

def list_count(length):
    while True:
        try:
            user_input = int(input(f'Enter the list count (must be less than {length}):\t'))
        
            if user_input > length:
                print(f'The list must be less than or equal to [bold][red]{length}[/red]![/bold]')
            else:
                return user_input
        except ValueError:
            print('[red]Value must be a number![/red]')
            continue

def menu():
    while True:
        print(f"\n[cyan]{banner}[/cyan]")
        print()
        print("1. Trending [yellow][bold]All[/bold][/yellow] (Movies + TV mixed list)")
        print("2. Trending [yellow][bold]Movies[/bold][/yellow]")
        print("3. Trending [yellow][bold]TV/Series[/bold][/yellow]")
        print("4. [red]Exit[/red]")
        
        choice = input("Enter your choice (eg: 2): ")

        if choice in ["1", "2", "3", "4"]:
            choice = int(choice)

            if choice == 1:
                ta = TrendingList(trending_all_url)
                all_data = ta.data()
                data = all_data["results"]
                ta.show_list(list_count(len(data)), data)

            elif choice == 2:
                tm = TrendingList(trending_movies_url)
                mv_data = tm.data()
                data = mv_data["results"]
                tm.show_list(list_count(len(data)), data)

            elif choice == 3:
                tt = TrendingList(trending_tv_url)
                tt_data = tt.data() 
                data = tt_data["results"]
                tt.show_list(list_count(len(data)), data)

            elif choice == 4:
                print("[green]Have a nice day![/green]")
                break

        else:
            print("[red]Invalid input, please enter a valid option.[/red]\n")

menu()