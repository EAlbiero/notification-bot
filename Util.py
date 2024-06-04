import json

class Util():

    file = "websites.json"
    websites = ""

    def loadWebsites(func):

        def load(*args, **kwargs):
            Util.websites = json.load(open(Util.file))
            func(*args, **kwargs)
            return func(*args, **kwargs)
        
        return load

        
    @loadWebsites
    def getWebsiteList():

        website_list = []
        
        for website in Util.websites.keys():
            website_list.append(website)
        
        return website_list
    
    @loadWebsites
    def getAccountsList(website: str):

        accounts_list = []

        for name in Util.websites[website].keys():
            accounts_list.append(name)

        return accounts_list
    
    @loadWebsites
    def addAccount(website: str, name: str, url: str):

        Util.websites[website][name] = url
        aux = json.dumps(Util.websites, indent=4)

        with open("websites.json", "w") as new_json:
            new_json.write(aux)


w = Util.getWebsiteList()

for i in w:
    print(i)

Util.addAccount('twitter', 'linkclick', 'linkclick-url')

for a in Util.getAccountsList('twitter'):
    print(a)