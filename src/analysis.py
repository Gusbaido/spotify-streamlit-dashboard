import pandas as pd
from collections import Counter
from typing import List, Dict, Any
from fetch import get_top_tracks 

def get_top_albums_from_tracks(tracks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Extrai os álbuns mais frequentes entre as faixas fornecidas.

    Args:
        tracks: Lista de dicionários com dados das faixas.

    Returns:
        Lista de dicionários com os álbuns, artista e número de faixas por álbum.
    """
    album_counter = Counter()

    for track in tracks:
        album = track.get("album", "Desconhecido")
        artista = track.get("artista", "Desconhecido")
        chave = (album, artista)
        album_counter[chave] += 1

    albuns_ordenados = sorted(album_counter.items(), key=lambda x: x[1], reverse=True)

    resultado = []
    for (album, artista), quantidade in albuns_ordenados:
        resultado.append({
            "album": album,
            "artista": artista,
            "quantidade_musicas": quantidade
        })

    return resultado

def analisar_albuns(tracks: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Analisa os álbuns mais frequentes nas top músicas do usuário.

    Args:
        tracks: Lista de dicionários contendo dados das músicas

    Returns:
        DataFrame com os álbuns mais ouvidos
    """
    print("Analisando álbuns mais ouvidos...")

    albuns = [track['album'] for track in tracks if 'album' in track]
    contagem = Counter(albuns)

    df_albuns = pd.DataFrame(contagem.items(), columns=["Álbum", "Quantidade"])
    df_albuns = df_albuns.sort_values(by="Quantidade", ascending=False).reset_index(drop=True)

    print("Análise concluída!")
    return df_albuns

def salvar_csv(df: pd.DataFrame, nome_arquivo: str = "albuns_mais_ouvidos.csv"):
    """
    Salva os dados analisados em um arquivo CSV.

    Args:
        df: DataFrame a ser salvo
        nome_arquivo: Nome do arquivo CSV
    """
    df.to_csv(nome_arquivo, index=False)
    print(f"Dados salvos em: {nome_arquivo}")

if __name__ == "__main__":
    from auth import spotify_auth

    sp = spotify_auth()
    top_tracks = get_top_tracks(sp, limit=50, time_range='medium_term')

    if top_tracks:
        df_resultado = analisar_albuns(top_tracks)
        print(df_resultado)
        salvar_csv(df_resultado)
    else:
        print("⚠️ Nenhuma faixa foi retornada para análise.")