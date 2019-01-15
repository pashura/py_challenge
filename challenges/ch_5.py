#  challenge 5

import requests
import pickle


def main():
    response = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
    got_list = pickle.loads(response.content)

    for i in got_list:
        print("".join(x[0] * x[1] for x in i))


if __name__ == "__main__":
    main()
