import streamlit as st
import spotipy
from typing import List, Dict, Any

@st.cache_data
def get_top_tracks(sp: spotipy.Spotify, limit: int = 50, time_range: str = 'medium_term') -> List[Dict[str, Any]]:
    """
    Busca as músicas mais ouvidas do usuário.
    """
    st.toast(f"📥 Buscando top {limit} músicas ({time_range})...")
    try:
        results = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    except Exception as e:
        st.error(f"❌ Erro ao buscar músicas: {e}")
        return []

    tracks = []
    for item in results['items']:
        track_info = {
            'name': item['name'],
            'artista': ', '.join([artist['name'] for artist in item['artists']]),
            'album': item['album']['name'],
            'popularity': item['popularity'],
            'artist_ids': [artist['id'] for artist in item['artists']],
            'album_id': item['album']['id']
        }
        tracks.append(track_info)

    st.toast(f"✅ {len(tracks)} músicas recuperadas.")
    return tracks

@st.cache_data
def get_album_covers(sp: spotipy.Spotify, tracks: List[Dict[str, Any]]) -> Dict[str, str]:
    """
    Extrai URLs das capas dos álbuns a partir das tracks.
    """
    if not tracks:
        return {}

    covers = {}
    album_ids = list(set(track['album_id'] for track in tracks if 'album_id' in track))

    # Busca informações dos álbuns em lotes (máximo 20 por vez)
    for i in range(0, len(album_ids), 20):
        batch = album_ids[i:i+20]
        try:
            albums_info = sp.albums(batch)
            for album in albums_info['albums']:
                if album and album['images']:
                    covers[album['name']] = album['images'][0]['url']
        except Exception as e:
            st.warning(f"Erro ao buscar lote de álbuns: {e}")
            continue

    return covers

@st.cache_data
def get_saved_albums(sp: spotipy.Spotify, limit: int = 20) -> List[Dict[str, Any]]:
    """
    Busca álbuns salvos pelo usuário.
    """
    try:
        results = sp.current_user_saved_albums(limit=limit)
        return [
            {
                "album": item["album"]["name"],
                "artista": item["album"]["artists"][0]["name"],
                "data_lancamento": item["album"]["release_date"],
                "capa": item["album"]["images"][0]["url"] if item["album"]["images"] else ""
            }
            for item in results["items"]
        ]
    except Exception as e:
        st.error(f"❌ Erro ao buscar álbuns salvos: {e}")
        return []


@st.cache_data
def get_saved_episodes(sp: spotipy.Spotify, limit: int = 20) -> List[Dict[str, Any]]:
    """
    Busca episódios de podcast salvos pelo usuário.
    """
    try:
        results = sp.current_user_saved_episodes(limit=limit)
        return [
            {
                "episodio": item["episode"]["name"],
                "podcast": item["episode"]["show"]["name"],
                "data": item["episode"]["release_date"]
            }
            for item in results["items"]
        ]
    except Exception as e:
        st.error(f"❌ Erro ao buscar episódios: {e}")
        return []


@st.cache_data
def get_top_artists(sp: spotipy.Spotify, time_range: str = "medium_term", limit: int = 20) -> List[Dict[str, Any]]:
    """
    Busca os artistas mais ouvidos pelo usuário.
    """
    try:
        results = sp.current_user_top_artists(time_range=time_range, limit=limit)
        return [
            {
                "nome": item["name"],
                "seguidores": item["followers"]["total"],
                "generos": ", ".join(item["genres"])
            }
            for item in results["items"]
        ]
    except Exception as e:
        st.error(f"❌ Erro ao buscar artistas: {e}")
        return []
