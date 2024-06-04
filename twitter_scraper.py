import json
from urllib.request import urlopen
import datetime as dt

websites = json.load(open("websites.json"))

for name, data in websites["twitter"].items():

    filter = ""
    for word in data['keywords'].split():
        filter += f"+{word}"
    filter = filter[1:]

    url = f"https://x.com/search?q=%22{filter}" + r"%22+%28from%3A" + f"{data['user']}%29+until%3A{(dt.datetime.today() + dt.timedelta(days=1)).strftime('%Y-%m-%d')}+since%3A{dt.datetime.today().strftime('%Y-%m-%d')}+-filter%3Areplies&src=typed_query"

    page = urlopen(url)

    print(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    start_index = html.find(f"View post analytics")
    print(html)
    print(html[start_index:30])



    

