import requests
from bs4 import BeautifulSoup


def parse():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mp_mv250'
    page = requests.get(url=url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    dictionary = {}

    name_block = soup.find_all('td', class_='titleColumn')
    name = []
    for item in name_block:  # заносим названия фильмов в массив
        name += [item.find('a').text]

    rating_block = soup.find_all('td', class_='ratingColumn imdbRating')
    rating = []
    for item in rating_block:  # заносим рейтинг в массив
        rating += [item.text.strip()]

    for i in range(250):  # заносим данные из массивов в словарь
        dictionary[name[i]] = rating[i]

    print(dictionary)


if __name__ == '__main__':
    parse()
