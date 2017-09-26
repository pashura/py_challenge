#  challenge 6

import requests
import zipfile


def main():
    response = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')

    with open("data/channel.zip", "wb") as code:
        code.write(response.content)

    channel_zip = zipfile.ZipFile('data/channel.zip')
    print([i.filename for i in channel_zip.filelist])
    print(channel_zip.read('readme.txt'))


if __name__ == '__main__':
    main()
