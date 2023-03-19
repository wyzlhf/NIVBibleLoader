import requests
import json
from typing import List,Dict


def get_books(url: str = 'https://www.biblegateway.com/audio/bible_data/?version=niv&author=dramatized') -> List[Dict[str,int]]:
    r: str = requests.get(url).text
    r_to_dict: dict = json.loads(r)
    books: List[Dict[str,int]] = r_to_dict["books"]
    return books


if __name__ == '__main__':
    get_books()
