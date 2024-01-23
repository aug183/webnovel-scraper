import requests
from bs4 import BeautifulSoup

chapternum = 1
url = "https://bonnovel.com/manga/i-really-am-not-the-lord-of-demon-novel/chapter-642_end/"
while (chapternum < 401):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    novel_text = soup.find("div", {"class": "reading-content"}).text

    chapter = open(f'Chapter{chapternum}.txt', 'a', encoding="utf-8")
    chapter.write(novel_text)
    chapter.close()
    a_tag = soup.find("a", {"class": "next_page"})
    url = a_tag['href']
    chapternum += 1