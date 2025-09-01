# 🎧 Spotify Dashboard Pessoal

Este projeto é um dashboard interativo em **Streamlit** que utiliza a **API do Spotify** para analisar suas músicas, artistas, álbuns e gêneros mais ouvidos. Ideal para demonstrar habilidades em **Python**, **análise de dados** e **visualizações interativas**.

O código foi refatorado para seguir as melhores práticas, garantindo maior clareza, eficiência e facilidade de deploy.

## 📌 Funcionalidades

- 🔐 Autenticação OAuth 2.0 segura com Spotipy.
- 🎶 Coleta das suas músicas mais ouvidas (curto, médio e longo prazo).
- 🎤 Identificação dos seus artistas e álbuns favoritos.
- 📊 Visualizações interativas com Plotly (artistas, álbuns e gêneros).
- 🖼️ Exibição das capas dos álbuns.
- ⚡ Caching de dados para uma experiência de usuário mais rápida.

## 🚀 Como Executar o Projeto Localmente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/spotify-dashboard.git
    cd spotify-dashboard
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure suas credenciais:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais da API do Spotify:
    ```env
    SPOTIPY_CLIENT_ID=sua_client_id
    SPOTIPY_CLIENT_SECRET=sua_client_secret
    SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
    ```

4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run main.py
    ```

## ☁️ Deploy no Streamlit Cloud

Para fazer o deploy deste dashboard na Streamlit Cloud, siga estes passos:

1.  **Faça o fork deste repositório** para a sua conta do GitHub.
2.  **Acesse a [Streamlit Cloud](https://share.streamlit.io/)** e conecte sua conta do GitHub.
3.  **Clique em "New app"** e selecione o seu repositório.
4.  **Configure os Secrets:** Em `Advanced settings...` > `Secrets`, adicione as mesmas credenciais do seu arquivo `.env`:
    ```toml
    SPOTIPY_CLIENT_ID = "sua_client_id"
    SPOTIPY_CLIENT_SECRET = "sua_client_secret"
    SPOTIPY_REDIRECT_URI = "sua_url_do_app_streamlit/callback"
    ```
    **Atenção:** A `SPOTIPY_REDIRECT_URI` deve ser a URL do seu aplicativo na Streamlit Cloud.

5.  **Clique em "Deploy!"** e aguarde a mágica acontecer.

## 🧠 Estrutura do Projeto (Refatorada)

```
.
├── main.py              # Script principal da aplicação Streamlit
├── auth.py              # Módulo de autenticação com o Spotify
├── fetch.py             # Funções para buscar dados da API do Spotify (com cache)
├── analysis.py          # Funções para analisar os dados brutos
├── visualizations.py    # Funções para criar os gráficos e visuais
├── requirements.txt     # Dependências do projeto
├── README.md            # Este arquivo
└── .env                 # Arquivo de credenciais (local, não versionado)
```

## 🛠 Tecnologias Usadas

-   Python 3.9+
-   Streamlit
-   Spotipy
-   Plotly Express
-   Pandas
-   python-dotenv

---

👤 **Autor Original:** Luis Gustavo Baido
⭐ **Refatoração:** Jules (Seu Assistente de IA)
