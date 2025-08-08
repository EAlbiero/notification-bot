import json, requests
from bs4 import BeautifulSoup

class Parser():
    file = "websites.json"
    log = "log.txt"


    def updateChapter(mangas: str):
        data = Parser.getData()

        for manga in mangas:
            data["manga"][manga]["chapter"] += 1
        with open(Parser.file, "w") as f:
            json.dump(data, f, indent=4)


    def checkForUpdates():
        updates = []
        data = Parser.getData()


        for manga in data["manga"]:

            chapter = data["manga"][manga]["chapter"]
            rurl = data["manga"][manga]["url"]+str(chapter)
            r = requests.get(rurl)
            if Parser.isChapterOut(r):
                updates.append(manga)

        if updates:
            Parser.updateChapter(updates)

        return updates


    def getData():
        f = Parser.file
        with open(f, 'r') as f_obj:
            data = json.load(f_obj)

        return data
    

    def isChapterOut(r: requests.Response):
        if (r.status_code != 200):
            return False
        
        soup = BeautifulSoup(r.text, 'html.parser')
        pages = soup.find_all(class_=['reading-content', 'js-pages-container', 'pages text-center', 'entry-content single-content', 'wp-manga-chapter-img'])
        if pages:
            pages = pages[0]
            print(r.url, len(pages.find_all(recursive=False)) > 5)
            return len(pages.find_all(recursive=False)) > 5
        return False