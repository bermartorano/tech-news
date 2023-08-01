import requests
import time
from bs4 import BeautifulSoup


def fetch(url: str) -> str:
    time.sleep(1)
    try:
        res = requests.get(
                            url,
                            headers={"user-agent": "Fake user-agent"},
                            timeout=3,
                            )
        res.raise_for_status()
        return res.text
    except requests.HTTPError as error:
        print('Erro HTTP', error)
        return None
    except requests.ReadTimeout:
        print('Tempo esgotado')
        return None


def scrape_updates(html_content):
    page = BeautifulSoup(html_content, "html.parser")
    all_h2_titles = page.find_all('h2', {'class': 'entry-title'})
    final_list = [h2_title.a.attrs['href'] for h2_title in all_h2_titles]
    return final_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
