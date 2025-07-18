import streamlit as st
from auth import spotify_auth
from fetch import get_top_tracks
from analysis import get_top_albums_from_tracks
import pandas as pd
import plotly.express as px

# Autenticação Spotify
sp = spotify_auth()

# Sidebar para seleção de período
time_range = st.sidebar.selectbox(
    "Selecione o período de análise:",
    options=["short_term", "medium_term", "long_term"],
    format_func=lambda x: {
        "short_term": "Últimas 4 semanas",
        "medium_term": "Últimos 6 meses",
        "long_term": "Todos os tempos"
    }[x]
)

st.title("Spotify Insights - Dashboard Pessoal")

# Tabs para seções
aba = st.tabs(["Top Músicas", "Top Álbuns", "Análises"])

with aba[0]:
    st.header("Suas Músicas Mais Ouvidas")
    tracks = get_top_tracks(sp, limit=50, time_range=time_range)
    df_tracks = pd.DataFrame(tracks)

    if not df_tracks.empty:
        fig = px.bar(
            df_tracks,
            x='nome',
            y='popularidade',
            hover_data=['artista', 'album'],
            title="Popularidade das Suas Músicas Mais Ouvidas",
            labels={"nome": "Música", "popularidade": "Popularidade"}
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df_tracks[["rank", "nome", "artista", "album", "popularidade"]])
    else:
        st.warning("Nenhuma música encontrada.")

with aba[1]:
    st.header("Álbuns Mais Frequentes nas Suas Músicas Top")
    top_albums = get_top_albums_from_tracks(tracks)
    df_albums = pd.DataFrame(top_albums)

    if not df_albums.empty:
        fig_album = px.bar(
            df_albums,
            x='album',
            y='quantidade_musicas',
            color='artista',
            title="Álbuns com Mais Músicas no Top 50",
            labels={"album": "Álbum", "quantidade_musicas": "Nº de Músicas"}
        )
        fig_album.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_album, use_container_width=True)
        st.dataframe(df_albums)
    else:
        st.warning("Nenhum dado de álbum encontrado.")

with aba[2]:
    st.header("Análise Geral")
    if not df_tracks.empty:
        st.subheader("Top 5 Artistas Frequentes")
        artistas = df_tracks['artista'].value_counts().head(5)
        fig_artistas = px.pie(
            names=artistas.index,
            values=artistas.values,
            title="Artistas Mais Frequentes no Top 50"
        )
        st.plotly_chart(fig_artistas)

        st.subheader("Duração Média das Músicas")
        duracao_media = df_tracks['duracao_ms'].mean() / 1000
        minutos = int(duracao_media // 60)
        segundos = int(duracao_media % 60)
        st.metric("Média de Duração", f"{minutos}:{segundos:02} min")
    else:
        st.info("Dados insuficientes para análise.")
