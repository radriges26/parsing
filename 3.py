from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml


def parse_page(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    site = 'superjob'
    vak_title = [i.text for i in soup.select('div.f-test-search-result-item h2._2rfUm a')]
    vak_url = ['https://kazan.superjob.ru/' + i['href'] for i in
               soup.select('div.f-test-search-result-item h2._2rfUm a')]
    vak_price = [i.text for i in soup.select('span.f-test-text-company-item-salary span._2Wp8I')]
    data_to_return = []
    for num, i in enumerate(vak_title):
        data_to_return.append({
            "site": site,
            "title": i,
            "url": vak_url[num],
            "price": vak_price[num]
        })
    return data_to_return


all_vak = []

for i in range(1, 3):
    url = 'https://kazan.superjob.ru/vakansii/developer.html?page={}'.format(i)
    vak_temp = parse_page(url)
    all_vak += vak_temp


pd.DataFrame(all_vak).to_csv('vak.csv', index=False)
