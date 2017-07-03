#  challenge 2

import requests
import re


def main():
    response = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
    data = re.search('<!--\n%.*-->', response.text, re.MULTILINE | re.DOTALL).group()
    result = ""
    for i in data:
        result += i if i.isalpha() else ''
    print(result)


if __name__ == '__main__':
    main()
