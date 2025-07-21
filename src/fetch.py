import spotipy
from typing import List, Dict, Any


def get_top_tracks(sp: spotipy.Spotify, limit: int = 50, time_range: str = 'medium_term') -> List[Dict[str, Any]]:
    """
    Busca as músicas mais ouvidas do usuário.
    """
    print(f"📥 Buscando top {limit} músicas ({time_range})...")
    try:
        results = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    except Exception as e:
        print(f"❌ Erro ao buscar músicas: {e}")
        return []

    tracks = []
    for idx, item in enumerate(results['items'], start=1):
        track_info = {
            'rank': idx,
            'nome': item['name'],
            'artista': item['artists'][0]['name'],
            'album': item['album']['name'],
            'album_images': item['album']['images'],
            'id': item['id'],
            'popularidade': item['popularity'],
            'duracao_ms': item['duration_ms']
        }
        tracks.append(track_info)

    print(f"✅ {len(tracks)} músicas recuperadas.")
    return tracks


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
        print(f"❌ Erro ao buscar álbuns salvos: {e}")
        return []


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
        print(f"❌ Erro ao buscar episódios: {e}")
        return []


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
        print(f"❌ Erro ao buscar artistas: {e}")
        return []