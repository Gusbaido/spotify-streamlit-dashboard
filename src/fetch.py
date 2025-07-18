import spotipy
from typing import List, Dict, Any

def get_top_tracks(sp: spotipy.Spotify, limit: int = 50, time_range: str = 'medium_term') -> List[Dict[str, Any]]:
    """
    Busca as músicas mais ouvidas do usuário.

    Args:
        sp: Objeto Spotipy autenticado
        limit: Quantidade de músicas (máximo 50)
        time_range: Período (short_term, medium_term, long_term)

    Returns:
        Lista de dicionários com informações das músicas
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
            'id': item['id'],
            'popularidade': item['popularity'],
            'duracao_ms': item['duration_ms']
        }
        tracks.append(track_info)

    print(f"✅ {len(tracks)} músicas recuperadas.")
    return tracks

