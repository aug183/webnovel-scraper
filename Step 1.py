import requests
from bs4 import BeautifulSoup
import time

chapternum = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
url = "https://freewebnovel.com/novel/"
for chapternum in range(1, 508):
    # Accessing the webpage
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    if r.status_code == 200:
        print(f"Successfully accessed {url}")
    else:
        print(f"Failed to access {url}. Status code: {r.status_code}")
    
    # Creating a new txt file
    chapter = open(f'Chapter{chapternum}.txt', 'a', encoding="utf-8")

    # Finding the Chapter Content
    novel_text = soup.find("div", {"id": "article"})

    # Finding the Chapter Title
    if novel_text:
        titleInBody = novel_text.find('h4')
        if titleInBody:
            title = titleInBody.get_text()
        else: 
            title = soup.find("span", {"class": "chapter"}).get_text()
            # if novel_title:
            #     title = novel_title['title']

    # Writing the Chapter Title
    chapter.write(title + '\n')

    if novel_text:
        paragraphs = novel_text.find_all('p')
        if len(paragraphs) == 0: # If there are no p tags found in the div, then it is probably written with <br /> between paragraphs of text
            for br in novel_text.find_all('br'):
                br.replace_with('\n')
            novel_text = novel_text.get_text() # Writing the content to the txt file
            chapter.write(novel_text)
        else:
            for p in paragraphs: # p tags are present in the div containing the chapter content
                paragraph_text = p.get_text() # Writing the content to the txt file
                chapter.write(paragraph_text + '\n')

    # Closing the txt file
    chapter.close()

    # Finding the next chapter from the "next" button in the page
    a_tag = soup.find("a", title = "Read Next chapter")
    url = "https://freewebnovel.com" + a_tag['href']
    
    # Delay of 1 second to avoid server timeout
    time.sleep(1)