import spotipy
import time
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

playlist_id = '' 
client_id = '' 
client_secret = '' 
username = ''

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.user_playlist_tracks(username, playlist_id, fields = 'items', limit=100,  market=None)

tids = []
names =[]
for i, t in enumerate(results['items']):
    names.append(t['track']['name'])
    tids.append(t['track']['uri'])


start = time.time()
tracks = sp.audio_features(tids)


features_list = []

for i, t in enumerate(tracks):
  features_list.append([names[i],tracks[i]['valence'], tracks[i]['acousticness'],
                                tracks[i]['danceability'], tracks[i]['energy'],
                                tracks[i]['instrumentalness'], tracks[i]['liveness'],
                                tracks[i]['speechiness']])


df = pd.DataFrame(features_list, columns=['nome', 'valence', 'acousticness',
                                                  'danceability', 'energy',
                                                  'instrumentalness', 'liveness',
                                                  'speechiness'])

df.to_csv('dados_musicas_{}.csv'.format(playlist_id), index=False, decimal = ",", sep = ";")
#df.to_csv('dados_musicas_{}.csv'.format(playlist_id), index=False, decimal = ".", sep = ",")
