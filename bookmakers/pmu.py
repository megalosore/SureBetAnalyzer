import requests
from bs4 import BeautifulSoup


class Pmu:
    name = "Pmu"
    websiteUrl = "https://paris-sportifs.pmu.fr/"
    sportsUrls = {
        "Football": ["https://paris-sportifs.pmu.fr/pari/sport/25/football"],
        "Tennis": ["https://paris-sportifs.pmu.fr/pari/sport/9/tennis"],
        "Basketball": ["https://paris-sportifs.pmu.fr/pari/sport/59/basket-euro",
                       "https://paris-sportifs.pmu.fr/pari/sport/12/basket-us"],
        # "Baseball": "https://paris-sportifs.pmu.fr/pari/sport/14/baseball",
        "Boxe/MMA": ["https://paris-sportifs.pmu.fr/pari/sport/11/boxe",
                     "https://paris-sportifs.pmu.fr/pari/sport/273/mma"],
        # "Cyclisme": ["https://paris-sportifs.pmu.fr/pari/sport/36/cyclisme"],
        "Football Americain": ["https://paris-sportifs.pmu.fr/pari/sport/164/football-am%C3%A9ricain"],
        "Football Australien": ["https://paris-sportifs.pmu.fr/pari/sport/270/football-australien"],
        # "Golf": ["https://paris-sportifs.pmu.fr/pari/sport/4/golf"],
        "Handball": ["https://paris-sportifs.pmu.fr/pari/sport/54/handball"],
        "Hockey": ["https://paris-sportifs.pmu.fr/pari/sport/160/hockey-sur-glace-eu",
                   "https://paris-sportifs.pmu.fr/pari/sport/161/hockey-sur-glace-us"],
        "RugbyXV": ["https://paris-sportifs.pmu.fr/pari/sport/8/rugby"],
        "RugbyXIII": ["https://paris-sportifs.pmu.fr/pari/sport/100/rugby-%C3%A0-xiii"],
        "Snooker": ["https://paris-sportifs.pmu.fr/pari/sport/159/snooker"],
        # "Hivers": ["https://paris-sportifs.pmu.fr/pari/sport/82/ski-alpin"]
        "Volleyball": ["https://paris-sportifs.pmu.fr/pari/sport/57/volley-ball"],
        # "Formule1" : ["https://paris-sportifs.pmu.fr/pari/competition/999/sports-m%C3%A9caniques/formule-1"],
        "Tennis de table": ["https://paris-sportifs.pmu.fr/pari/sport/77/tennis-de-table"]

    }
    cote = {}

    def __init__(self):
        self.requestAllCote()

    def __str__(self):
        strReturn = ''
        for sport in self.cote:
            for key, value in self.cote[sport].items():
                strReturn += sport + "| " + key + "| " + str(value) + "\n"
        return strReturn

    def requestAllCote(self):
        for sport in self.sportsUrls:
            self.requestCote(sport)

    def requestCote(self, sport):
        self.cote[sport] = {}
        urlList = self.sportsUrls[sport]
        for url in urlList:
            head = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
            response = requests.get(url, headers=head)
            htmlToParse = BeautifulSoup(response.content, "lxml")
            matchSelector = ".pmu-event-list-grid-highlights-formatter-row.event-list-event-row"
            out = htmlToParse.select(matchSelector)
            for match in out:
                nameSelector = ".trow--event--name span"
                coteSelector = "ul li a"
                matchName = match.select_one(nameSelector).text.replace("//", "-")
                matchCotes = match.select(coteSelector)
                cotes = []
                for rawCote in matchCotes:
                    parsedCote = rawCote.text.replace(" ", "").replace("\n", "").replace(",", '.')
                    if parsedCote != "Accéderaudirect":
                        cotes.append(float(parsedCote))
                if matchName not in self.cote[sport]:
                    self.cote[sport][matchName] = cotes
                else:
                    self.cote[sport]["Duplicate " + matchName] = cotes

    def getCote(self):
        return self.cote

    def getCoteBySport(self, sport):
        return self.cote[sport]
