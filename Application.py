import requests
from dotenv import load_dotenv
import os
from src.TrendingList import TrendingList

load_dotenv()
API_KEY = os.getenv('API_KEY')

trending_all_url = "https://api.themoviedb.org/3/trending/all"
trending_movies_url = 'https://api.themoviedb.org/3/trending/movie'
trending_tv_url = "https://api.themoviedb.org/3/trending/tv/"

tm = TrendingList(trending_movies_url)
ta = TrendingList(trending_all_url)
tt = TrendingList(trending_tv_url)

mv_data = tm.data()
print(f"Movies: {mv_data['page']}")

all_data = ta.data()
print(f"All: {all_data['page']}")

tt_data = tt.data() 
print(f"Series/TV: {tt_data['page']}")