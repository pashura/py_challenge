#  challenge 6

import requests
import zipfile


def main():
    response = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')

    with open("data/channel.zip", "wb") as code:
        code.write(response.content)

    channel_zip = zipfile.ZipFile('data/channel.zip')
    # print([i.filename for i in channel_zip.filelist])
    # print(channel_zip.read('readme.txt'))

    # for i in channel_zip.filelist:
    #     if '90052' in str(i):
    #         print(channel_zip.open(i).read())

    nothing = '90052'
    # next_nothing = ''.join([i for i in response.text if i.isnumeric()])
    response = str(channel_zip.open('{}.txt'.format(nothing)).read())
    print(response)
    while 'Next nothing' in str(channel_zip.open('{}.txt'.format(nothing)).read()):
        response = channel_zip.open('{}.txt'.format(nothing)).read()
        print(nothing)
        print(response)
        nothing = ''.join([i for i in response if i.isnumeric()])



if __name__ == '__main__':
    main()
