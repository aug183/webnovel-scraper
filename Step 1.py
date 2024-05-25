import requests
from bs4 import BeautifulSoup
import time

chapternum = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
url = "https://novelbin.englishnovel.net/novel-book/lord-of-mysteries-2-circle-of-inevitability/chapter-1-1-foreigners"
while (chapternum < 782):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')


    if r.status_code == 200:
        print(f"Successfully accessed {url}")
    else:
        print(f"Failed to access {url}. Status code: {r.status_code}")
    
    
    novel_text = soup.find("div", {"class": "chr-c"})
    if novel_text:
        paragraphs = novel_text.find_all('p')
    #print(novel_text)

    chapter = open(f'Chapter{chapternum}.txt', 'a', encoding="utf-8")
    for p in paragraphs:
        paragraphs_text = p.get_text()
        chapter.write(paragraphs_text + '\n')
    chapter.close()
    a_tag = soup.find("a", {"id": "next_chap"})
    url = a_tag['href']
    chapternum += 1
    time.sleep(2)