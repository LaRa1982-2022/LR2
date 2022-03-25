from bs4 import BeautifulSoup as BS
import requests


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


for p in range(1, 34):
    url = f'https://prodaman.ru/safonova/books/Lunnyj-veter?page={p}'

    soup = BS(get_html(url), 'lxml')
    r = soup.find('div', class_='blog-text noselect reader-box')
    with open('out.txt', 'a', encoding='utf-8') as f:
        for i in r:
            print(i, file=f)

    soup = BS(get_html(url), 'lxml')
    r = soup.find('div', class_='blog-text noselect reader-box')
    with open('out.txt', 'a', encoding='utf-8') as f:
        for i in r:
            print(i, file=f)