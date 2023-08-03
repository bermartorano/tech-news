from tech_news.database import db
import re


def search_by_title(title):
    rgx = re.compile(f'{title}', re.IGNORECASE)
    query = list(db.news.find({'title': {'$regex': rgx}},
                              {'title': True, 'url': True, '_id': False}))
    result = [(news['title'], news['url']) for news in query]
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
