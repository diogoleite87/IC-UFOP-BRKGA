print("Executando...")

# install.packages("AER")
# install.packages("tidyverse")
# install.packages("wordcloud2")
# install.packages("gghighlight")
# install.packages("lubridate")
# install.packages("patchwork")
# install.packages("dplyr")
# install.packages("kableExtra")
# install.packages("tibble")
# install.packages("spotifyr")

library(AER)
library(tidyverse)
library(wordcloud2)
library(gghighlight)
library(lubridate)
library(patchwork)
library(dplyr)
library(kableExtra)
library(tibble)
library(spotifyr)

Sys.setenv(SPOTIFY_CLIENT_ID = "")
Sys.setenv(SPOTIFY_CLIENT_SECRET = "")
playlist_id <- ""
playlist_name <- "PROJETO UFOP"

access_token <- get_spotify_access_token()

dados <- get_playlist_audio_features(playlist_name, playlist_id) %>%
       unnest(track.artists) %>% 
       distinct(track.id, .keep_all = TRUE) %>%
       select(added_at, track.id, track.name,
              artist.id = id, artist.name = name,
              track.album.name, track.album.release_date, track.album.release_date_precision,
              track.popularity, danceability, energy, loudness, speechiness, acousticness,
              instrumentalness, liveness, valence, tempo
       ) %>%
       rowwise() %>%
       mutate(
              genres = str_flatten(get_artist(artist.id)$genres, collapse = ","),
              artist.popularity = get_artist(artist.id)$popularity
       )

print("Exibindo dados importantes coletados...")

print(dados[3])
print(dados[10])
print(dados[11])
print(dados[12])
print(dados[13])
print(dados[14])
print(dados[15])
print(dados[16])
print(dados[17])

print("Gravando dados...")

write.csv(dados, file = "") # caminho do arquivo