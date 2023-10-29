from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

# =============== Top 100 Billboard Web scraping =========
URL_billboard = "https://www.billboard.com/charts/hot-100/"
YOUR_CLIENT_ID = '361a69dfcb584e2583e934f70d3739b3'
YOUR_CLIENT_SECRET = 'd728602f938b4ad28174f0a7569c1e41'

date = input("What year do you want to travel to? Type the date in this format, YYYY-MM-DD: ")
year = date[:4]

response = requests.get(f"{URL_billboard}{date}/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

scraped = [song.getText().strip("\n") for song in soup.find_all(name="h3", class_="c-title", id="title-of-a-story")][5:]

scraped_art = [artist.getText().strip("\n") for artist in soup.find_all(name="span", class_="c-label")]

song_names = [name.replace("'", "").replace("!", "") for name in scraped
              if 'Songwriter(s):' not in name
              if 'Producer(s):' not in name
              if 'Imprint/Promotion Label:' not in name
              if 'Additional Awards' not in name
              ][:100]

artist_names = [artist.split(" Featuring")[0].split(" Duet")[0].replace("Ke$ha", "Kesha") for artist in scraped_art
                if not artist.isnumeric()
                if artist != "-"
                if artist != "NEW"
                if 'ENTRY' not in artist
                ]

# # ==================== Spotify API =======================

redirect = "http://example.com"


spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=YOUR_CLIENT_ID,
                                           client_secret=YOUR_CLIENT_SECRET,
                                           redirect_uri=redirect,
                                           scope="playlist-modify-private",
                                           cache_path="token.txt")

# spotify.get_access_token()

sp = spotipy.Spotify(oauth_manager=spotify_auth)

user_name = sp.current_user()["display_name"]
user_id = sp.current_user()["id"]

song_urls = []
for song, artist in zip(song_names, artist_names):
    items = sp.search(q=f"track: {song} artist: {artist}", type="track")["tracks"]["items"]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)