import streamlit as st
import pandas as pd
import plotly.express as px

from auth import spotify_auth
import fetch
import analysis
from visualizations import (
    plot_genre_distribution,
    plot_top_artists_bar,
    render_album_covers
)

st.set_page_config(page_title="🎵 Análise Musical Spotify", layout="wide")
st.title("Meu Perfil Musical no Spotify")

try:
    # Autenticação centralizada
    sp = spotify_auth()
    if not sp:
        st.error("Falha na autenticação com o Spotify. Verifique suas credenciais.")
        st.stop()
except Exception as e:
    st.error(f"Erro inesperado na autenticação: {e}")
    st.stop()

# --- Sidebar para filtros ---
st.sidebar.header("🔍 Filtros")
time_range_options = {
    "Curto Prazo (4 semanas)": "short_term",
    "Médio Prazo (6 meses)": "medium_term",
    "Longo Prazo (vários anos)": "long_term"
}
selected_range_key = st.sidebar.selectbox(
    "Período de Análise",
    list(time_range_options.keys())
)
time_range = time_range_options[selected_range_key]
limit = st.sidebar.slider(
    "Número de músicas para analisar",
    min_value=10, max_value=50, value=20, step=5
)

# --- Carregamento e Análise de Dados ---
# Usando as funções refatoradas e com cache
try:
    tracks = fetch.get_top_tracks(sp, limit=limit, time_range=time_range)
    if tracks:
        df_artists = analysis.analyze_artists_from_tracks(tracks)
        df_albums = analysis.analyze_albums_from_tracks(tracks)
    else:
        st.warning("Nenhuma música encontrada para o período selecionado.")
        st.stop()
except Exception as e:
    st.error(f"Ocorreu um erro ao buscar ou analisar os dados: {e}")
    st.stop()

# --- Interface com Abas ---
st.header("Explorando seu Perfil Musical")
tabs = st.tabs(["🎵 Músicas", "🎤 Artistas", "📀 Álbuns", "📊 Gêneros"])

# Aba 1: Músicas
with tabs[0]:
    st.subheader("Minhas Músicas Mais Ouvidas")
    if tracks:
        df_tracks = pd.DataFrame(tracks)
        # Ajuste para usar os nomes de coluna corretos de fetch.py
        st.dataframe(df_tracks[['name', 'artista', 'album', 'popularity']])
        st.caption(f"Exibindo as {len(tracks)} músicas mais ouvidas.")
    else:
        st.info("Não há dados de músicas para exibir.")

# Aba 2: Artistas
with tabs[1]:
    st.subheader("Meus Artistas Mais Ouvidos")
    if not df_artists.empty:
        fig_artists = plot_top_artists_bar(df_artists)
        st.plotly_chart(fig_artists, use_container_width=True)
        st.dataframe(df_artists)
    else:
        st.info("Não há dados de artistas para exibir.")

# Aba 3: Álbuns
with tabs[2]:
    st.subheader("Álbuns Mais Frequentes")
    if not df_albums.empty:
        fig_albums = px.bar(
            df_albums,
            x='album',
            y='quantidade_musicas',
            color='artista',
            title="Álbuns com Mais Músicas no Top",
            labels={"album": "Álbum", "quantidade_musicas": "Nº de Músicas"}
        )
        st.plotly_chart(fig_albums, use_container_width=True)

        # Exibição de capas
        album_covers = fetch.get_album_covers(sp, tracks)
        if album_covers:
            render_album_covers(album_covers)
    else:
        st.info("Não há dados de álbuns para exibir.")

# Aba 4: Gêneros
with tabs[3]:
    st.subheader("Distribuição de Gêneros Musicais")
    if tracks:
        fig_genres = plot_genre_distribution(sp, tracks)
        if fig_genres:
            st.plotly_chart(fig_genres, use_container_width=True)
        else:
            st.warning("Não foi possível gerar o gráfico de gêneros.")
    else:
        st.info("Não há dados de gêneros para analisar.")
