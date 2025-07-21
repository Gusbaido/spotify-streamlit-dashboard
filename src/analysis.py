def analyze_top_tracks(sp, limit=20, time_range='medium_term'):
    """
    Analisa as top tracks do usuário
    """
    try:
        # Busca top tracks
        results = sp.current_user_top_tracks(limit=limit, time_range=time_range)
        
        tracks = []
        artists_count = {}
        albums_count = {}
        
        for item in results['items']:
            # Dados da música
            track_data = {
                'name': item['name'],
                'artist': ', '.join([artist['name'] for artist in item['artists']]),
                'album': item['album']['name'],
                'popularity': item['popularity'],
                'artist_ids': [artist['id'] for artist in item['artists']],
                'album_id': item['album']['id']
            }
            tracks.append(track_data)
            
            # Conta artistas
            for artist in item['artists']:
                artist_name = artist['name']
                artists_count[artist_name] = artists_count.get(artist_name, 0) + 1
            
            # Conta álbuns
            album_name = item['album']['name']
            album_artist = item['artists'][0]['name']  # Primeiro artista
            albums_count[(album_name, album_artist)] = albums_count.get((album_name, album_artist), 0) + 1
        
        # Formata dados dos artistas
        artists = [{'name': name, 'count': count} for name, count in artists_count.items()]
        
        # Formata dados dos álbuns
        albums = [{'album': album, 'artist': artist, 'count': count} 
                 for (album, artist), count in albums_count.items()]
        
        return tracks, artists, albums
        
    except Exception as e:
        raise Exception(f"Erro ao analisar tracks: {e}")

def get_top_albums_from_tracks(tracks):
    """
    Extrai álbuns mais frequentes das tracks
    """
    try:
        if not tracks:
            return []
            
        album_count = {}
        for track in tracks:
            album_key = (track['album'], track['artist'].split(',')[0].strip())
            album_count[album_key] = album_count.get(album_key, 0) + 1
        
        albums = []
        for (album, artist), count in album_count.items():
            albums.append({
                'album': album,
                'artista': artist,
                'quantidade_musicas': count
            })
        
        return sorted(albums, key=lambda x: x['quantidade_musicas'], reverse=True)
        
    except Exception as e:
        raise Exception(f"Erro ao processar álbuns: {e}")

def get_album_covers_from_tracks(sp, tracks):
    """
    Extrai URLs das capas dos álbuns a partir das tracks e dos dados da API
    """
    try:
        if not tracks:
            return {}
            
        covers = {}
        
        # Extrai IDs únicos dos álbuns
        album_ids = set()
        for track in tracks:
            if 'album_id' in track:
                album_ids.add(track['album_id'])
        
        # Busca informações dos álbuns em lotes (máximo 20 por vez)
        album_ids_list = list(album_ids)
        
        for i in range(0, len(album_ids_list), 20):  # API permite max 20 álbuns por vez
            batch = album_ids_list[i:i+20]
            try:
                albums_info = sp.albums(batch)
                for album in albums_info['albums']:
                    if album and album['images']:
                        # Pega a primeira imagem (geralmente a de melhor qualidade)
                        cover_url = album['images'][0]['url']
                        covers[album['name']] = cover_url
            except Exception as e:
                print(f"Erro ao buscar lote de álbuns: {e}")
                continue  # Pula este lote se houver erro
        
        return covers
        
    except Exception as e:
        raise Exception(f"Erro ao obter capas: {e}")