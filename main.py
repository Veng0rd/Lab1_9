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
    for item in name_block:
        name += [item.find('a').text]

    rating = []
    rating_block = soup.find_all('td', class_='ratingColumn imdbRating')
    for item in rating_block:
        print(item.text.strip())


    # try:
    #     for item in block:
    #         # dictionary[item.find_next('a').text] = item.find_next(class_='ratingColumn imdbRating').text.strip()
    #         print(item.find_next() , '\n\n\n\n')
    #
    # except AttributeError:
    #     pass

    print(dictionary)


if __name__ == '__main__':
    parse()
