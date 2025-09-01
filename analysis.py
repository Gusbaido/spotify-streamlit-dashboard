import pandas as pd
from collections import Counter

def analyze_artists_from_tracks(tracks):
    """
    Analisa e conta os artistas a partir de uma lista de músicas.
    """
    if not tracks:
        return pd.DataFrame(columns=['name', 'count'])

    artist_list = [track['artista'] for track in tracks]
    artist_counts = Counter(artist_list)

    if not artist_counts:
        return pd.DataFrame(columns=['name', 'count'])

    df_artists = pd.DataFrame(artist_counts.items(), columns=['name', 'count'])
    return df_artists.sort_values('count', ascending=False)

def analyze_albums_from_tracks(tracks):
    """
    Analisa e conta os álbuns a partir de uma lista de músicas.
    """
    if not tracks:
        return pd.DataFrame(columns=['album', 'artista', 'quantidade_musicas'])

    album_counter = Counter()
    for track in tracks:
        album_key = (track['album'], track['artista'])
        album_counter[album_key] += 1

    if not album_counter:
        return pd.DataFrame(columns=['album', 'artista', 'quantidade_musicas'])

    albums_data = [{
        'album': key[0],
        'artista': key[1],
        'quantidade_musicas': count
    } for key, count in album_counter.items()]

    df_albums = pd.DataFrame(albums_data)
    return df_albums.sort_values('quantidade_musicas', ascending=False)
