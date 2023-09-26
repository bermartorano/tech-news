# 🗞️💻 Tech News

Neste projeto, costrui uma aplicação capaz de fazer raspagem de dados no blog de notícias da escola de programação Trybe e as salvar em um banco de dados. Também foram desenvolvidas funções para procurar notícias salvas no banco, seja por categoria, data ou título.

## 🛠️ Ferramentas Utilizadas:
* Python
* MongoDB
* pymongo
* beautifulsoup4

## ▶️ Como Executar a Aplicação
1. Clone o repositório.
2. Na raiz do projeto, crie e entre no ambiente virtual `python3 -m venv .venv && source .venv/bin/activate`.
3. Instale as dependências `python3 -m pip install -r dev-requirements.txt`.
4. Suba o container do banco `docker-compose up -d mongodb`.
5. Para realizar a raspagem de dados, na raiz do projeto:
   * Inicie um terminal interativo python: `python3 -i tech_news/scraper.py`.
   * Execute a função para a raspagem: `get_tech_news(n)`, em que `n` é um número inteiro de notícias a serem raspadas.

## Detalhes dos Requisitos:
![image](https://github.com/bermartorano/tech-news/assets/110858573/e5592fa6-943e-4621-aee6-af693eaeec65)
