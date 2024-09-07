from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.billboard.com/charts/hot-100/"
top_hits_date = input("What day would you like to musically travel to? (YYYY-MM-DD) ]")

response = requests.get(f"{BASE_URL}{top_hits_date}")
soup = BeautifulSoup(response.text, 'html.parser')

top_hits_data = soup.select("li ul li h3")
songs = [song.getText().strip() for song in top_hits_data]

print(songs)
