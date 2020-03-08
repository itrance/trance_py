import requests
from bs4 import BeautifulSoup


MAIN_URL_WALL_1 = 'http://wallpaperswide.com/page/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
           'Accept': '*/*'}
start_page = int(input('First page: '))
end_page = int(input('Last page: '))


def get_html(url):
    r = requests.post(url)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='thumb')
    pictures = []
    for item in items:
        with_dot_html = item.find('a').get('href')
        pictures.append(
            'http://wallpaperswide.com/download' + with_dot_html[:len(with_dot_html) - 16] + '-3840x2160.html')
    for aaa in pictures:
        if requests.get(aaa).status_code == 200 :
            name_of_pict = aaa[35:len(aaa) - 5]
            image_to_download = requests.get(aaa, stream=True)
            fi = open(name_of_pict + '.jpg', 'wb')
            fi.write(image_to_download.content)
            image_to_download.close()
            print(f'{aaa} download successful')
        else:
            pass


def parse():
    global start_page
    while start_page <= end_page:
        MAIN_URL_WALL = MAIN_URL_WALL_1 + str(start_page)
        html = get_html(MAIN_URL_WALL)
        if html.status_code == 200:
            print(f'Downloading from {start_page} page...')
            get_content(html.text)
            start_page += 1
        else:
            print(f'\nPage not foud')
    print("Downloading is complete")


parse()