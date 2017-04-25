import requests
from bs4 import BeautifulSoup


def getHtml(url):
    page = requests.get(url)
    print(page.text)

def get1024():
    for i in range(1, 5):
        url = "http://t66y.com/thread0806.php?fid=22&search=&page=" + str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.text)
        print(soup)

get1024()