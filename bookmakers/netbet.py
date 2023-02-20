import requests
from bs4 import BeautifulSoup


class Netbet:
    name = "Netbet"
    websiteUrl = "https://www.netbet.fr/"
    cote = {}
    sportsUrls = {
        "Football": ["https://www.netbet.fr/morecomingevents?sportid=13&limit=1000&offset=0"],
        "Tennis": ["https://www.netbet.fr/morecomingevents?sportid=21&limit=1000&offset=0"],
        "Basketball": ["https://www.netbet.fr/morecomingevents?sportid=4&limit=1000&offset=0"],
        "Boxe/MMA": ["https://www.netbet.fr/morecomingevents?sportid=23&limit=1000&offset=0",
                     "https://www.netbet.fr/morecomingevents?sportid=78&limit=1000&offset=0"],
        "Badminton" : ["https://www.netbet.fr/morecomingevents?sportid=35&limit=1000&offset=0"],
        # "Cyclisme": ["https://paris-sportifs.pmu.fr/pari/sport/36/cyclisme"],
        "Football Americain": ["https://www.netbet.fr/morecomingevents?sportid=7&limit=1000&offset=0"],
        "Football Australien": ["https://www.netbet.fr/morecomingevents?sportid=1&limit=1000&offset=0"],
        # "Golf": ["https://paris-sportifs.pmu.fr/pari/sport/4/golf"],
        "Handball": ["https://www.netbet.fr/morecomingevents?sportid=9&limit=1000&offset=0"],
        "Hockey": ["https://www.netbet.fr/morecomingevents?sportid=10&limit=1000&offset=0"],
        "RugbyXV": ["https://www.netbet.fr/morecomingevents?sportid=12&limit=1000&offset=0"],
        "RugbyXIII": ["https://www.netbet.fr/morecomingevents?sportid=38&limit=1000&offset=0"],
        "Snooker": ["https://www.netbet.fr/morecomingevents?sportid=20&limit=1000&offset=0"],
        "Volleyball": ["https://www.netbet.fr/morecomingevents?sportid=14&limit=1000&offset=0"],
        # "Formule1" : ["https://www.zebet.fr/fr/sport/32-formule_1"],
        "Tennis de table": ["https://www.netbet.fr/morecomingevents?sportid=26&limit=1000&offset=0"]
    }

    def __init__(self):
        self.requestAllCote()

    def requestAllCote(self):
        for sport in self.sportsUrls:
            self.requestCote(sport)

    def requestCote(self, sport):
        self.cote[sport] = {}
        req = requests.Session()
        head = {
            'Host': 'www.netbet.fr',
            'Content-Length': '0',
            'Origin': 'https://www.netbet.fr',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.netbet.fr/football',
            'Cookie': 'sticky=balancer.wsnb5; nb-ipclient=2a02:6ea0:dc05::a15e',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest'
        }
        urlList = self.sportsUrls[sport]
        for url in urlList:
            response = req.get(url, headers=head)
            data = response.json()
            for htmlMatch in data:
                parsedMatch = BeautifulSoup(htmlMatch, "lxml")
                nameSelector = ".nb-match_actor"
                oddSelector = ".nb-odds_amount"
                matchName = parsedMatch.select(nameSelector)[0].text + " - " + parsedMatch.select(nameSelector)[1].text
                matchCotes = parsedMatch.select(oddSelector)
                cotes = []
                for rawCote in matchCotes:
                    parsedCote = rawCote.text.replace(" ", "").replace("\n", "").replace(",", '.')
                    if parsedCote != "Accéderaudirect":
                        cotes.append(float(parsedCote))
                if matchName not in self.cote[sport]:
                    self.cote[sport][matchName] = cotes
                else:
                    self.cote[sport]["Duplicate "+matchName] = cotes

    def __str__(self):
        strReturn = ''
        for sport in self.cote:
            for key, value in self.cote[sport].items():
                strReturn += sport + "| " + key + "| " + str(value) + "\n"
        return strReturn

    def getCote(self):
        return self.cote

    def getCoteBySport(self, sport):
        return self.cote[sport]
