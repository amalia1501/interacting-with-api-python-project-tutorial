import os
import pandas as pd
# import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

client_id = os.environ.get('78b07631aa7f45619f30648a3fec32aa')
client_secret = os.environ.get('b15d856616fc4d068ff0dae2e610a7d5')

# Paso 4: Inicializar la biblioteca Spotipy

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

con = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = '78b07631aa7f45619f30648a3fec32aa',
                                                              client_secret = 'b15d856616fc4d068ff0dae2e610a7d5'))
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

# Paso 5: Realizar solicitudes a la API

results = con.search(q="Bohemian Rhapsody", type="track")

# Get the first track from the results
track = results['tracks']['items'][6]

# Print the track name
print(track['name'])

# artist_id = "3TVXtAsR1Inumwj472S9r4"

# response = con.artist_top_tracks("3TVXtAsR1Inumwj472S9r4")
# if response:
#   # We keep the "tracks" object of the answer
#   tracks = response["tracks"]
#   # We select, for each song, the data we are interested in and discard the rest
#   tracks = [{k: (v/(1000*60))%60 if k == "duration_ms" else v for k, v in track.items() if k in ["name", "popularity", "duration_ms"]} for track in tracks]