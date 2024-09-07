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
    return sp

target_date = input("What day would you like to musically travel to? (YYYY-MM-DD) ]")
year = target_date.split('-')[0]
songs = get_top_100_songs_for_date(target_date)

# generate Spotify API token
spotify = get_spotify_token()

song_urls = []
for song in songs:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        url = result["tracks"]["items"][0]["uri"]
        song_urls.append(url)
    except IndexError:
        print(f"'{song}' not found in Spotify, skipping.")

# create Spotify playlist
playlist = spotify.user_playlist_create(user=os.getenv('SPOTIFY_DISPLAY_NAME'), name=f"{target_date} Billboard 100", public=False)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_urls)
