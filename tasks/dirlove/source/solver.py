# -*- coding:utf-8 -*-

import requests as req


def process(url):
    letters = [chr(c) for c in range(97, 123)]
    letters.append('-')

    for letter in letters:
        r = req.get(url+f'{letter}/')
        if len(r.url) > len(url):
            print(r.url)
            process(r.url)


if __name__ == '__main__':
    process('http://surctf.ru:1336/')
