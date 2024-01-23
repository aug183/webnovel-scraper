from pyexpat import features
import requests
from bs4 import BeautifulSoup

chapternum = 1
while (chapternum < 401):
    #url = "https://bonnovel.com/manga/i-really-am-not-the-lord-of-demon-novel/chapter-642_end/"
    url = "https://noveltop1.net/novel-book/the-book-eating-magician/chapter-" + str(chapternum) + "/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    novel_text = soup.find("div", {"class": "reading-content"}).text

    chapter = open(f'Chapter{chapternum}.txt', 'a', encoding="utf-8")
    chapter.write(novel_text)
    chapternum += 1