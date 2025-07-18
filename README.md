<<<<<<< HEAD
🎧 Spotify Dashboard Pessoal
Este projeto é um dashboard interativo em Streamlit que utiliza a API do Spotify para analisar suas músicas e álbuns mais ouvidos. Ideal para quem quer apresentar habilidades em Python, APIs, análise de dados e visualização interativa no portfólio.

📌 Funcionalidades
Autenticação com OAuth (Spotipy)

Coleta das 50 músicas mais ouvidas do usuário

Análise dos álbuns mais frequentes

Visualização com gráficos interativos (Plotly)

Métricas como artistas mais presentes e tempo médio das músicas

🚀 Como Executar o Projeto

1. Clone o Repositório
git clone https://github.com/seu-usuario/spotify-dashboard.git
cd spotify-dashboard

2. Instale as dependências
Use pip para instalar as bibliotecas necessárias:
pip install -r requirements.txt

3. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com suas credenciais do Spotify:
SPOTIPY_CLIENT_ID=sua_client_id
SPOTIPY_CLIENT_SECRET=sua_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback

4. Rode o aplicativo
streamlit run main.py

🧠 Estrutura do Projeto
📁 src/
│
├── auth.py              # Realiza a autenticação OAuth com o Spotify
├── fetch.py             # Faz a coleta de músicas mais ouvidas
├── analysis.py          # Processa os dados para gerar insights e rankings
├── main.py              # Dashboard principal com Streamlit
├── .env                 # Suas credenciais (não subir ao GitHub!)
└── requirements.txt     # Bibliotecas do projeto

📊 Visão Geral do Dashboard

🔹 Aba 1: Top Músicas
Gráfico de barras com popularidade das músicas

Tabela com rank, nome, artista, álbum e popularidade

🔹 Aba 2: Top Álbuns
Gráfico de barras mostrando álbuns com mais músicas no Top 50

Tabela detalhada com nome do álbum, artista e quantidade de faixas

🔹 Aba 3: Análises
Gráfico de pizza com os 5 artistas mais recorrentes

Duração média das músicas exibida com métrica interativa

🛠 Tecnologias Usadas
Python 3.10+

Streamlit

Spotipy (API Spotify)

Plotly Express

Pandas

dotenv

🧩 Próximos Passos
Você pode expandir o projeto com:

Análise de gêneros musicais

Comparativo por tempo (gráfico de radar entre os períodos)

Histórico de escuta ao longo do tempo

Download de relatórios em CSV

Versão pública hospedada (Streamlit Cloud ou Hugging Face Spaces)

💼 Objetivo
Este projeto foi desenvolvido para fins de portfólio e prática com:

APIs e autenticação OAuth

Pipeline de análise de dados

Gráficos interativos para storytelling

Aplicações Web com Python

👤 Autor
Gustavo Baido
• Analista de Dados | Desenvolvedor de Projetos em Python & Streamlit

=======
# spotify-streamlit-dashboard
Análise interativa dos hábitos musicais usando a API do Spotify, Python, Spotipy, Streamlit e Plotly.
>>>>>>> 0feb2a20e35cb3e3875eb4d1ea9f0579dd059288
