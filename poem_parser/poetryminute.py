import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.poetryminute.org'
AUTHOR = 'author'
DATE = 'date'
CATEGORY = 'category'
TITLE = 'title'
BASE_DIR = 'poems-by-'
DIRS = {
    AUTHOR: '-'.join([BASE_DIR, AUTHOR]),
    DATE: '-'.join([BASE_DIR, DATE]),
    CATEGORY: '-'.join([BASE_DIR, CATEGORY]),
    TITLE: '-'.join([BASE_DIR, TITLE])
}
BLOG_DIV = 'blog_div_text'


def get_page_by_dir(dir):
    full_url = '/'.join([BASE_URL, DIRS[dir]])
    resp = requests.get(full_url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    div = soup.find(attrs={"class": BLOG_DIV}).children
    collection = {}
    month = ''
    l_poems = []
    for child in div:
        if child.name == 'h2':
            month = child.string
        elif child.name == 'ul':
            for li in child.find_all('li'):
                l_poems = collection.get(month, [])
                link = li.a['href']
                text = li.string
                text = text.replace('\xa0', ' ')
                title, author = text.rsplit(' by ', 1)
                d = {
                    'link': link,
                    'title': title,
                    'author': author,
                }
                l_poems.append(d)
                collection[month] = l_poems
        # elif child.next == 'h2':
        #     collection[month] = d
        else:
            continue
    return l_poems
