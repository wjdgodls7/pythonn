import requests
from bs4 import BeautifulSoup

종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']


def result(구멍):

    data = requests.get('https://finance.naver.com/item/sise.nhn?code={구멍}')
    soup = BeautifulSoup(data.content, 'html.parser')
    # print(soup.find_all('span', class_='tah')[5].text)
    return soup.find_all('strong', id="_nowVal")[0].text


f = open('a.txt', 'w')
for i in 종목들:
    f.write(result(i))
f.close()
