import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Carregar variáveis do .env
load_dotenv()

# Obter credenciais do ambiente
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

# Escopo necessário para acessar top músicas
scope = "user-top-read"

def spotify_auth():
    """
    Realiza autenticação com o Spotify e retorna o cliente autenticado.
    """
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        show_dialog=True  # Garante que a permissão seja solicitada sempre
    )
    sp = Spotify(auth_manager=auth_manager)
    return sp

