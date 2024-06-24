import json
import requests

class Util():
    file = "websites.json"

    def updateChapter(mangas):
        data = Util.getData()

        for manga in mangas:
            data["manga"][manga]["chapter"] += 1
        with open(Util.file, "w") as f:
            json.dump(data, f, indent=4)

    def checkForUpdates():
        updates = []
        data = Util.getData()

        for manga in data["manga"]:
            rurl = data["manga"][manga]["url"]+str(data["manga"][manga]["chapter"])
            r = requests.get(rurl)

            # Casos em que o site redireciona para Home ao invés de retornar 404
            if (r.status_code == 200) and (rurl == r.url[:-1]):
                updates.append(manga)

        if updates:
            Util.updateChapter(updates)
        return updates

    def getData(f = "websites.json"):
        with open(f, 'r') as f_obj:
            data = json.load(f_obj)

        return data

