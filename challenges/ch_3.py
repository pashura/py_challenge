#  challenge 3

import requests
import re


def main():
    response = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
    response_data = re.search(
        "<!--\n.*-->", response.text, re.MULTILINE | re.DOTALL
    ).group()
    result_list = re.findall(
        "[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", response_data, re.MULTILINE
    )
    result = "".join(result_list)
    print(result)


if __name__ == "__main__":
    main()
