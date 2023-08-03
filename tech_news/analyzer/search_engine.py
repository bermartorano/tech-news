from tech_news.database import db
from datetime import datetime
import re


def search_by_title(title):
    rgx = re.compile(f'{title}', re.IGNORECASE)
    query = list(db.news.find({'title': {'$regex': rgx}},
                              {'title': True, 'url': True, '_id': False}))
    result = [(news['title'], news['url']) for news in query]
    return result


def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        date_in_db_format = date_obj.strftime('%d/%m/%Y')
        query = list(db.news.find({'timestamp': date_in_db_format},
                                  {'title': True, 'url': True, '_id': False}))
        result = [(news['title'], news['url']) for news in query]
    except ValueError:
        raise ValueError('Data inválida')
    return result


# Requisito 9
def search_by_category(category):
    rgx = re.compile(f'{category}', re.IGNORECASE)
    query = list(db.news.find({'category': {'$regex': rgx}},
                              {'title': True, 'url': True, '_id': False}))
    result = [(news['title'], news['url']) for news in query]
    return result
