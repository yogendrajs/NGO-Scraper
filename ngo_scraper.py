import requests, json, os, pprint
from os import path
from bs4 import BeautifulSoup

file = path.exists('ngo_scraper.json')
if file:
    with open('ngo_scraper.json', "r+") as content:
        load = json.load(content)
        print (load)
else:
    url = requests.get("https://www.giveindia.org/certified-indian-ngos")
    # print (url.status_code)
    parse = BeautifulSoup(url.text, "html.parser")

    table = parse.find('table', class_ = "jsx-697282504 certified-ngo-table")
    trs = table.find_all('tr')

    total = []
    for tr in trs:
        td = tr.find_all('td')
        for i in td:
            if i.text:
                total.append(i.text)
    # print (total)

    places = []
    for tr in trs:
        td = tr.find_all('td')
        for i in range(len(td)):
            if i == 2:
                places.append(td[i].text)
    # print (places)
    maindics = {}
    for i in range(len(places)):
        list1 = []
        for j in range(len(total)):
            if places[i] == total[j]:
                list1.append(total[j-2])
        maindics[places[i]] = list1
    # print (maindics)
    dump = json.dumps(maindics)
    with open('ngo_scraper.json', 'w') as f:
        f.write(dump)
