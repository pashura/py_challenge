#  challenge 0

import requests

def main():
    response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
    print(response.text)

    #test


if __name__ == '__main__':
    main()
