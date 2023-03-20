import bs4
import requests
import json
from typing import List, Dict
from bs4 import BeautifulSoup


def get_books(url: str = 'https://www.biblegateway.com/audio/bible_data/?version=niv&author=dramatized') -> List[
    Dict[str, str]]:
    r: str = requests.get(url).text
    r_to_dict: dict = json.loads(r)
    books: List[Dict[str, str]] = r_to_dict["books"]
    return books


def join_to_chapter_url(chapter: str, paragraph: int,
                        basic_url: str = 'https://www.biblegateway.com/audio/dramatized/niv/') -> str:
    chapter_url: str = basic_url + chapter + '.' + str(paragraph)
    return chapter_url


def get_mp3_url(url: str='https://www.biblegateway.com/audio/dramatized/niv/2Sam.1') -> str:
    r = requests.get(url).text
    soup: BeautifulSoup = BeautifulSoup(r, features="lxml")
    tag_audio: bs4.element.Tag = soup.audio.source.attrs
    # tag_audio_to_soup=BeautifulSoup(tag_audio)
    mp3_src: str = tag_audio['src']

    return mp3_src


def load_mp3(chapter_name: str, paragrph: int, url: str, save_path: str = '.') -> None:
    r = requests.get(url)
    mp3_name: str = chapter_name + '.' + str(paragrph) + '.mp3'
    save_path = save_path + '/' + mp3_name
    # all_path:str=sa
    with open(save_path, "wb") as f:
        f.write(r.content)


def get_all_mp3():
    print('*************************开始下载*************************')
    books: List[Dict[str, str]] = get_books()
    for book in books:
        book_name: str = book['book']
        real_book_name: str = book['display']
        total_paragrph: int = int(book['chapters'])
        for i in range(total_paragrph):
            print(f'开始下载{book_name}章第{i + 1}节')
            chapter_url = join_to_chapter_url(book_name, i + 1)
            mp3_src = get_mp3_url(chapter_url)
            print('mp3的链接是：', mp3_src)
            load_mp3(real_book_name, i + 1, mp3_src)
    print('*************************下载结束*************************')


if __name__ == '__main__':
    get_all_mp3()
    # print(get_mp3_url())
