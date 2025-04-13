import re
import requests
from requests import RequestException


def get_page(url: str) -> str:
    resp = requests.get(url)
    if resp.ok:
        return resp.text
    else:
        raise requests.exceptions.RequestException

def parse_page(hypertext):
    pattern = r"<a.*href=\"([^\"]*)\""
    return re.findall(pattern, hypertext)


def main(url1: str, url2: str):
    page_a = get_page(url1)
    urls = parse_page(page_a)
    for url in urls:
        replaced_url = url.replace("stepic", "stepik")
        print(replaced_url)
        if replaced_url == url2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    try:
        url_a = input()
        url_b = input()
        main(url_a, url_b)
    except RequestException as e:
        print(e)

# https://stepik.org/media/attachments/lesson/24472/sample0.html
# https://stepik.org/media/attachments/lesson/24472/sample2.html
# https://stepik.org/media/attachments/lesson/24472/sample1.html