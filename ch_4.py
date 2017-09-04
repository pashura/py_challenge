#  challenge 4

import requests


def main():
    response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
    next_nothing = ''.join([i for i in response.text if i.isnumeric()])

    while ''.join([i for i in response.text if i.isnumeric()]) != '' or 'Divide' in response.text:
        response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(next_nothing))
        print(response.text)
        if 'Divide' in response.text:
            next_nothing = 8022
        elif '82683' in response.text:
            next_nothing = 63579
        else:
            next_nothing = ''.join([i for i in response.text if i.isnumeric()])


if __name__ == '__main__':
    main()
