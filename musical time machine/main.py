from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100/"

def get_top_100_songs_for_date(date):
    response = requests.get(f"{BILLBOARD_BASE_URL}{date}")
    soup = BeautifulSoup(response.text, 'html.parser')
    top_hits_data = soup.select("li ul li h3")
    return [song.getText().strip() for song in top_hits_data]


def get_spotify_token():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            show_dialog=True,
            cache_path="token.txt",
            username=os.getenv('SPOTIFY_DISPLAY_NAME')
        )
    )
    return sp.current_user()['id']

target_date = input("What day would you like to musically travel to? (YYYY-MM-DD) ]")
songs = get_top_100_songs_for_date(target_date)

# generate Spotify API token
# get_spotify_token()

