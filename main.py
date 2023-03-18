#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys
import json

headers = {'User-Agent': 'Mozilla/5.0'}


def find_word(word):
    print(f'Looking for the word "{word}" in Merriam-Webster...')
    url = f"https://www.merriam-webster.com/dictionary/{word}"

    with requests.session() as session:
        translation_page = requests.get(url)
        translation_page.raise_for_status()
        soup = BeautifulSoup(translation_page.content, 'html.parser')

        json_str = json.loads(soup.find(type="application/ld+json").contents[0])

        audio_download_url = json_str[4]['contentURL']
        audio_file = session.get(audio_download_url)
        audio_file.raise_for_status()
        with open(f"/Users/bochkovoy/Downloads/{word}.mp3", 'wb') as file:
            file.write(audio_file.content)
        print("Done!")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        word_inp = sys.argv[1]
        find_word(word_inp)
    elif len(sys.argv) > 2:
        print("Wrong number of arguments!")
        exit()

    while True:
        word_inp = input("Enter word to search for: ")
        find_word(word_inp)

