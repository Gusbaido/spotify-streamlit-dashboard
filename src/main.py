import streamlit as st
import pandas as pd
import plotly.express as px

from auth import spotify_auth
from analysis import analyze_top_tracks, get_top_albums_from_tracks, get_album_covers_from_tracks
from visualizations import (
    plot_genre_distribution,
    plot_top_artists_bar,
    render_album_covers
)

st.set_page_config(page_title="🎵 Análise Musical Spotify", layout="wide")
st.title("Meu Perfil Musical no Spotify")

try:
    sp = spotify_auth()
except Exception as e:
    st.error(f"Erro na autenticação: {e}")
    st.stop()

# Tradução de períodos
time_range_options = {
    "Curto Prazo (4 semanas)": "short_term",
    "Médio Prazo (6 meses)": "medium_term",
    "Longo Prazo (vários anos)": "long_term"
}

# Sidebar
st.sidebar.header("🔍 Filtros")
selected_range = st.sidebar.selectbox("Período de Análise", list(time_range_options.keys()))
time_range = time_range_options[selected_range]

limit = st.sidebar.slider("Número de músicas", min_value=10, max_value=50, step=10, value=20)

# Dados com tratamento de erro
try:
    tracks, artists, albums = analyze_top_tracks(sp, limit=limit, time_range=time_range)
except Exception as e:
    st.error(f"Erro ao obter dados: {e}")
    st.stop()

# Abas
aba = st.tabs(["🎵 Músicas", "📀 Álbuns", "🎤 Artistas", "📊 Gêneros"])

# 🎵 Músicas
with aba[0]:
    st.header("Minhas Músicas Mais Ouvidas")
    if tracks:
        df_tracks = pd.DataFrame(tracks)
        st.dataframe(df_tracks[["name", "album", "artist", "popularity"]])
        st.caption("As músicas mais ouvidas no período selecionado.")
    else:
        st.warning("Nenhuma música encontrada.")

# 📀 Álbuns
with aba[1]:
    st.header("Álbuns Mais Frequentes nas Minhas Músicas Top")
    if tracks:
        top_albums = get_top_albums_from_tracks(tracks)
        df_albums = pd.DataFrame(top_albums)

        if not df_albums.empty:
            fig_album = px.bar(
                df_albums,
                x='album',
                y='quantidade_musicas',
                color='artista',
                title="Álbuns com Mais Músicas no Top",
                labels={"album": "Álbum", "quantidade_musicas": "Nº de Músicas"}
            )
            fig_album.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_album, use_container_width=True)
            st.dataframe(df_albums)

            # Exibe as capas dos álbuns - CORRIGIDO: agora passa o parâmetro sp
            try:
                album_covers = get_album_covers_from_tracks(sp, tracks)
                render_album_covers(album_covers)
            except Exception as e:
                st.error(f"Erro ao carregar capas: {e}")
        else:
            st.warning("Nenhum dado de álbum encontrado.")
    else:
        st.warning("Nenhuma música disponível para análise de álbuns.")

# 🎤 Artistas
with aba[2]:
    st.header("Meus Artistas Mais Ouvidos")
    if artists:
        df_artists = pd.DataFrame(artists)
        try:
            fig_artists = plot_top_artists_bar(df_artists)
            if fig_artists is not None:
                st.plotly_chart(fig_artists, use_container_width=True)
            else:
                st.error("Erro na criação do gráfico de artistas")
        except Exception as e:
            st.error(f"Erro no gráfico de artistas: {e}")
        st.dataframe(df_artists)
    else:
        st.warning("Nenhum artista encontrado.")

# 📊 Gêneros
with aba[3]:
    st.header("Distribuição de Gêneros Musicais")
    if tracks:
        try:
            fig_genres = plot_genre_distribution(sp, tracks)
            if fig_genres is not None:
                st.plotly_chart(fig_genres, use_container_width=True)
            else:
                st.error("Não foi possível criar o gráfico de gêneros")
        except Exception as e:
            st.error(f"Erro no gráfico de gêneros: {e}")
    else:
        st.warning("Nenhuma música disponível para análise de gêneros.")