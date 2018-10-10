import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.poetryminute.org'
AUTHOR = 'author'
DATE = 'date'
CATEGORY = 'category'
TITLE = 'title'
BASE_DIR = 'poems-by'
DIRS = {
    AUTHOR: '-'.join([BASE_DIR, AUTHOR]),
    DATE: '-'.join([BASE_DIR, DATE]),
    # CATEGORY: '-'.join([BASE_DIR, CATEGORY]),
    TITLE: '-'.join([BASE_DIR, TITLE])
}
BLOG_DIV = 'blog_div_text'


def get_poems():
    collection = {}
    for poem_dir in DIRS:
        full_url = '/'.join([BASE_URL, DIRS[poem_dir]])
        resp = requests.get(full_url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        div = soup.find(attrs={"class": BLOG_DIV}).children
        category = ''
        d_category = {}
        for child in div:
            if child.name == 'h2':
                category = child.string
            elif child.name == 'ul':
                for li in child.find_all('li'):
                    l_poems = d_category.get(category, [])
                    link = li.a['href']
                    text = li.string or li.text
                    text = text.replace('\xa0', ' ')
                    if ' by ' in text:
                        title, author = text.rsplit(' by ', 1)
                    else:
                        title = text
                    author = ''
                    if poem_dir == AUTHOR:
                        author = category
                    d = {
                        'link': link,
                        'title': title,
                        'author': author,
                    }
                    l_poems.append(d)
                    d_category[category] = l_poems
            # elif child.next == 'h2':
            #     collection[month] = d
            else:
                continue
        collection[poem_dir] = d_category
    return collection
