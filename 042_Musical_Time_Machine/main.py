import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
from ytmusicapi import YTMusic

# This solution uses a predetermined date due to limited dates available on the website.

date = "2024-06-29"
url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
response = requests.get(url)
# pprint(response.text)

soup = BeautifulSoup(response.text, "lxml")
# Find all the song entries on the page
song_titles = soup.find_all(name="h3", class_="chart-entry__title")
song_titles_text = [song.getText().strip() for song in song_titles]
# pprint(song_titles_text)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")
# pprint(playlists)

# Create a new Playlist
playlist_name = f"Hot 100 - {date}"
playlist_description = f"Top 100 songs from {date}."

playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == playlist_name:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        playlist_name,
        playlist_description,
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

for song in song_titles_text:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")