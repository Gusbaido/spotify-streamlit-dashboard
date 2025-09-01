import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import pandas as pd

def plot_top_artists_bar(df_artists):
    """
    Cria gráfico de barras dos artistas mais ouvidos
    """
    try:
        if df_artists.empty:
            return None
            
        # Verifica se as colunas necessárias existem
        required_columns = ['name', 'count']
        if not all(col in df_artists.columns for col in required_columns):
            return None
            
        # Ordena por contagem e pega os top 10
        df_sorted = df_artists.sort_values('count', ascending=False).head(10)
        
        fig = px.bar(
            df_sorted,
            x='count',
            y='name',
            orientation='h',
            title="Top Artistas Mais Ouvidos",
            labels={'count': 'Número de Músicas', 'name': 'Artista'},
            color='count',
            color_continuous_scale='Viridis'
        )
        
        fig.update_layout(
            height=500,
            yaxis={'categoryorder': 'total ascending'},
            showlegend=False
        )
        
        return fig
    
    except Exception as e:
        st.error(f"Erro na criação do gráfico de artistas: {e}")
        return None

def plot_genre_distribution(sp, tracks):
    """
    Cria gráfico de distribuição de gêneros
    """
    try:
        if not tracks:
            return None
            
        # Coleta gêneros de todos os artistas
        all_genres = []
        
        # Extrai IDs únicos dos artistas
        artist_ids = set()
        for track in tracks:
            if 'artist_ids' in track:
                artist_ids.update(track['artist_ids'])
        
        # Busca informações dos artistas em lotes
        artist_ids_list = list(artist_ids)
        
        for i in range(0, len(artist_ids_list), 50):  # API permite max 50 por vez
            batch = artist_ids_list[i:i+50]
            try:
                artists_info = sp.artists(batch)
                for artist in artists_info['artists']:
                    if artist and 'genres' in artist:
                        all_genres.extend(artist['genres'])
            except Exception as e:
                continue  # Pula este lote se houver erro
        
        if not all_genres:
            # Se não conseguiu pegar gêneros da API, cria dados fictícios
            fig = go.Figure()
            fig.add_annotation(
                text="Não foi possível obter informações de gêneros",
                xref="paper", yref="paper",
                x=0.5, y=0.5,
                showarrow=False,
                font=dict(size=16)
            )
            fig.update_layout(
                title="Distribuição de Gêneros Musicais",
                height=400
            )
            return fig
        
        # Conta os gêneros
        genre_counts = Counter(all_genres)
        top_genres = dict(genre_counts.most_common(10))
        
        # Cria DataFrame
        df_genres = pd.DataFrame(
            list(top_genres.items()), 
            columns=['genero', 'quantidade']
        )
        
        # Cria gráfico de pizza
        fig = px.pie(
            df_genres,
            values='quantidade',
            names='genero',
            title="Distribuição dos Top 10 Gêneros Musicais"
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=500)
        
        return fig
    
    except Exception as e:
        st.error(f"Erro na análise de gêneros: {e}")
        
        # Retorna gráfico vazio em caso de erro
        fig = go.Figure()
        fig.add_annotation(
            text=f"Erro ao processar gêneros: {str(e)[:100]}...",
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=14)
        )
        fig.update_layout(
            title="Distribuição de Gêneros Musicais",
            height=400
        )
        return fig

def render_album_covers(album_covers):
    """
    Renderiza as capas dos álbuns
    """
    try:
        if not album_covers:
            st.info("Nenhuma capa de álbum disponível.")
            return
            
        st.subheader("📀 Capas dos Álbuns")
        
        # Organiza em colunas
        cols = st.columns(min(4, len(album_covers)))
        
        for i, (album_name, cover_url) in enumerate(album_covers.items()):
            with cols[i % len(cols)]:
                if cover_url:
                    st.image(cover_url, caption=album_name, width=150)
                else:
                    st.text(f"📀 {album_name}")
                    
    except Exception as e:
        st.error(f"Erro ao renderizar capas: {e}")