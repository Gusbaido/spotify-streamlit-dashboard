# 🎧 Spotify Dashboard Pessoal

Este projeto é um dashboard interativo em **Streamlit** que utiliza a **API do Spotify** para analisar suas músicas, artistas, álbuns e gêneros mais ouvidos. Ideal para demonstrar habilidades em **Python**, **API REST**, **OAuth 2.0**, **análise de dados** e **visualizações interativas** com Plotly.

## 📌 Funcionalidades

- 🔐 Autenticação com OAuth usando Spotipy  
- 🎶 Coleta de até 50 músicas mais ouvidas (curto, médio e longo prazo)  
- 📀 Análise dos álbuns mais recorrentes  
- 🎤 Identificação dos artistas mais escutados  
- 🧬 Gráfico de distribuição de gêneros musicais  
- 📊 Visualização com gráficos interativos (Plotly)  
- 🖼️ Exibição das capas dos álbuns  
- 📋 Tabelas interativas com os principais dados musicais  

## 🚀 Como Executar o Projeto

1. **Clone o repositório**


git clone https://github.com/seu-usuario/spotify-dashboard.git
cd spotify-dashboard
Instale as dependências

pip install -r requirements.txt


Configure o arquivo .env

Crie um arquivo .env na raiz com suas credenciais do Spotify:
env
SPOTIPY_CLIENT_ID=sua_client_id
SPOTIPY_CLIENT_SECRET=sua_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
Execute o Streamlit
streamlit run main.py

🧠 Estrutura do Projeto
📁 src/
│
├── auth.py              # Autenticação OAuth com Spotipy
├── analysis.py          # Funções de extração e análise de dados do Spotify
├── visualizations.py    # Criação dos gráficos e exibição de imagens
├── main.py              # Interface principal com Streamlit
├── .env                 # Credenciais de acesso (não subir ao GitHub!)
└── requirements.txt     # Bibliotecas utilizadas

📊 Visão Geral do Dashboard
🔹 Aba 1: Músicas Tabela com título, artista, álbum e popularidade

🔹 Aba 2: Álbuns Gráfico de barras dos álbuns mais presentes no top Capas dos álbuns renderizadas com Streamlit

🔹 Aba 3: Artistas Gráfico horizontal dos 10 artistas mais ouvidos

🔹 Aba 4: Gêneros Gráfico de pizza com os gêneros musicais predominantes

🛠 Tecnologias Usadas
Python 3.10+

Streamlit

Spotipy

Plotly Express

Pandas

dotenv

🧩 Próximos Passos
🔍 Filtros por período customizado

📈 Comparação entre intervalos (ex: gráfico de radar)

🧠 Dashboard com histórico de escuta

📤 Exportação de relatórios em CSV

☁️ Versão pública hospedada (Streamlit Cloud ou Hugging Face Spaces)

💼 Objetivo
Este projeto foi desenvolvido para fins de estudo, prática e apresentação de:

Integração com API 

Autenticação OAuth segura

Pipeline de análise de dados musicais

Visualização de dados interativa

Desenvolvimento de apps com Python e Streamlit

👤 Autor
Luis Gustavo Baido | Analista de Dados | Desenvolvedor Python & Streamlit 
📬linkedin./luis-gustavo-santos-baido-a0aa47159 🌐 github.com/Gusbaido
