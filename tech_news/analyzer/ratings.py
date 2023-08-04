from tech_news.database import db


def top_5_categories():
    all_news = db.news.find()
    category_count = {}
    # separar a função que conta as categorias
    for news in all_news:
        try:
            category_count[news['category']] += 1
        except KeyError:
            category_count[news['category']] = 1
    category_count_list = list(category_count.items())
    ctg_list_ordered = sorted(category_count_list,
                              key=lambda ctg: (-ctg[1], ctg[0]))
    final_list = []
    five_or_less = 5 if len(ctg_list_ordered) > 5 else len(ctg_list_ordered)
    for index in range(five_or_less):
        final_list.append(ctg_list_ordered[index][0])
    return final_list
