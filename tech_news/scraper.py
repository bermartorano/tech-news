import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news


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
    all_links = [h2_title.a.attrs['href'] for h2_title in all_h2_titles]
    return all_links


def scrape_next_page_link(html_content):
    page = BeautifulSoup(html_content, "html.parser")
    next_page_a_tag = page.find('a', {'class': 'next page-numbers'})
    result = next_page_a_tag.attrs['href'] if next_page_a_tag else None
    return result


def scrape_news(html_content):
    page = BeautifulSoup(html_content, "html.parser")
    final_dict = {
    }
    url = page.find(
        'div', {'class': 'post-sidebar-inner'}
        ).div['data-share-url']
    final_dict['url'] = url
    final_dict['title'] = page.find('h1',
                                    {'class': 'entry-title'}).text.strip()
    final_dict['timestamp'] = page.find('li', {'class': 'meta-date'}).text
    final_dict['writer'] = page.find('span', {'class': 'author'}).a.text

    read_time_text = page.find('li', {'class': 'meta-reading-time'}).text
    final_dict['reading_time'] = int(read_time_text.split()[0])
    final_dict['summary'] = page.find(
            'div',
            {'class': 'entry-content'}
        ).p.text.strip()
    category_link = page.find('div', {'class': 'meta-category'}).a
    final_dict['category'] = category_link.find_all('span')[1].text
    return final_dict


def get_tech_news(amount):
    news_scraped = []
    initial_page_url = 'https://blog.betrybe.com/'
    current_news_page = fetch(initial_page_url)
    all_news_links = scrape_updates(current_news_page)
    current_news_index = 0
    for news_index in range(amount):
        if current_news_index >= len(all_news_links):
            next_page_url = scrape_next_page_link(current_news_page)
            current_news_page = fetch(next_page_url)
            all_news_links = scrape_updates(current_news_page)
            current_news_index = 0
        news_html_content = fetch(all_news_links[current_news_index])
        news = scrape_news(news_html_content)
        news_scraped.append(news)
        current_news_index += 1
    create_news(news_scraped)
    return news_scraped
