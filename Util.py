import json
import requests
import time

class Util():
    file = "websites.json"
    log = "log.txt"

    def updateChapter(mangas: str):
        data = Util.getData()

        for manga in mangas:
            data["manga"][manga]["chapter"] += 1
        with open(Util.file, "w") as f:
            json.dump(data, f, indent=4)

    def checkForUpdates():
        updates = []
        data = Util.getData()

        Util.logActivity("Looking for updates")

        for manga in data["manga"]:

            chapter = data["manga"][manga]["chapter"]

            rurl = data["manga"][manga]["url"]+str(chapter)
            r = requests.get(rurl)

            Util.logActivity(f"Trying to find chapter {chapter} from {manga}.\tURL: {rurl}")

            # Casos em que o site redireciona para Home ao invés de retornar 404
            if (Util.isChapterOut(r)) and (rurl == r.url[:-1]):
                updates.append(manga)

                Util.logActivity("Chapter found!")

        if updates:
            Util.logActivity("Updating .json file")
            Util.updateChapter(updates)
            Util.logActivity("Finished updating .json file")
            Util.logActivity("Returning all updates found")
        else:
            Util.logActivity("No updates where found, returning an empty list")

        return updates

    def getData(f = "websites.json"):
        with open(f, 'r') as f_obj:
            data = json.load(f_obj)

        return data
    
    def isChapterOut(r: requests.Response):
        if (r.status_code == 200) and (r.text.count("image") > 5):
            return True
        return False
    
    def logActivity(msg: str):
        with open(Util.log, 'a') as log_file:
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]:\t{msg}\n")



