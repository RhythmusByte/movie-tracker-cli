import requests
from dotenv import load_dotenv
import os
from src.TrendingList import TrendingList

load_dotenv()
API_KEY = os.getenv('API_KEY')

trending_all_url = "https://api.themoviedb.org/3/trending/all"
trending_movies_url = 'https://api.themoviedb.org/3/trending/movie'
trending_tv_url = "https://api.themoviedb.org/3/trending/tv"

banner = """
┌─────────────────────────┐
│ Movie Tracker CLI       │
│ Track • Discover • List │
└─────────────────────────┘
"""

def menu():
    while True:
        print(f"\n{banner}")
        print()
        print("1. Trending All (Movies + TV mixed list)")
        print("2. Trending Movies")
        print("3. Trending TV/Series")
        print("4. Exit")
        
        choice = input("Enter your required list (eg: 2): ")

        if choice in ["1", "2", "3", "4"]:
            choice = int(choice)

            if choice == 1:
                ta = TrendingList(trending_all_url)
                all_data = ta.data()
                ta.show_list(all_data["results"])

            elif choice == 2:
                tm = TrendingList(trending_movies_url)
                mv_data = tm.data()
                tm.show_list(mv_data["results"])

            elif choice == 3:
                tt = TrendingList(trending_tv_url)
                tt_data = tt.data() 
                tt.show_list(tt_data["results"])

            elif choice == 4:
                print("Have a nice day!")
                break

        else:
            print("Invalid input, please enter a valid option.\n")

menu()