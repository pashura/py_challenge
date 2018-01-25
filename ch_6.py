#  challenge 6

import requests
import zipfile


def main():
    response = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')

    with open("data/channel.zip", "wb") as code:
        code.write(response.content)

    channel_zip = zipfile.ZipFile('data/channel.zip')

    nothing = '90052'

    arr_nothings = []
    while 'Next nothing' in str(channel_zip.open('{}.txt'.format(nothing)).read()):
        response = channel_zip.open('{}.txt'.format(nothing)).read()
        arr_nothings.append(nothing)

        nothing = ''.join([i for i in response.decode('utf8') if i.isnumeric()])

    arr_result = []

    for i in arr_nothings:
        for info in channel_zip.infolist():
            if str(info.filename).strip('.txt') == str(i):
                arr_result.append(info.comment.decode())

    # hockey = ''.join(arr_result)
    # print(hockey)

    result = ''.join(alpha for alpha in dict.fromkeys(arr_result).keys() if alpha.isalpha())
    print(result)


if __name__ == '__main__':
    main()
