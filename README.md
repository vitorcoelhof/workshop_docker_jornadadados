# Workshop Docker - Jornada de Dados

Este projeto é uma aplicação web interativa desenvolvida em Python com Streamlit, voltada para demonstração de dashboards, gráficos e métricas em tempo real, pronta para ser executada em ambiente Docker. O app pode ser acessado no link:  https://workshop-docker-jornadadados.onrender.com/ (irá expirar em alguns dias hehe)

Imagem do frontend:

<img width="1868" height="882" alt="image" src="https://github.com/user-attachments/assets/94987799-e32f-456b-a806-35aa62b31c7a" />


## Estrutura do Projeto

```
workshop_docker/
├── app.py           # Código principal da aplicação Streamlit
├── Dockerfile       # Dockerfile para build da imagem
├── pyproject.toml   # Gerenciamento de dependências (Poetry)
├── poetry.lock      # Lockfile do Poetry
├── .dockerignore    # Arquivos/pastas ignorados no build
├── .gitignore       # Arquivos/pastas ignorados no git
├── .python-version  # Versão do Python utilizada
├── .venv/           # Ambiente virtual (local)
└── README.md        # Documentação do projeto
```

## Principais Funcionalidades
- Interface moderna e responsiva com Streamlit
- Dashboard de métricas em tempo real
- Gráficos interativos (Plotly)
- Customização de temas e estilos
- Seção de feedback do usuário
- Pronto para deploy em Docker

## Como Executar

### Usando Docker (Recomendado)
1. Certifique-se de ter Docker instalado.
2. Na raiz do projeto, execute:
   ```bash
   docker build -t workshop-docker .
   docker run -p 8501:8501 workshop-docker
   ```
3. Acesse a aplicação em: http://localhost:8501

### Executando Localmente (sem Docker)
1. Crie e ative um ambiente virtual Python 3.12+
2. Instale as dependências com Poetry:
   ```bash
   poetry install
   ```
3. Execute a aplicação:
   ```bash
   poetry run streamlit run app.py
   ```
4. Acesse em: http://localhost:8501

## Sobre o Código
- O arquivo `app.py` traz uma interface visual com métricas, gráficos radar, dashboard, temas customizados e seção de feedback.
- O Dockerfile automatiza o build e execução da aplicação em container.
- As dependências são gerenciadas via Poetry (ver `pyproject.toml`).

---
Este projeto é ideal para quem deseja aprender a criar e publicar aplicações de dados modernas com Python, Streamlit e Docker.
