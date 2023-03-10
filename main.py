#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys

headers = {'User-Agent': 'Mozilla/5.0'}


def find_word(word):
    print(f"Looking for the word {word} in Merriam-Webster...")

    url = f"https://media.merriam-webster.com/audio/prons/en/us/mp3/{word[0]}/{word}001.mp3"
    with requests.session() as session:
        audio_file = session.get(url)
        with open(f"/Users/bochkovoy/Downloads/{word}.mp3", 'wb') as file:
            file.write(audio_file.content)
        print("Done!")


if __name__ == '__main__':
    word_inp = sys.argv[1]
    find_word(word_inp)
