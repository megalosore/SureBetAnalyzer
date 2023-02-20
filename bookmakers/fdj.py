import requests
from bs4 import BeautifulSoup


class Fdj:
    name = "Fdj"
    websiteUrl = "https://www.enligne.parionssport.fdj.fr/"
    cote = {}
    sportsUrls = {
        "Football": ["https://www.enligne.parionssport.fdj.fr/paris-football"],
        "Tennis": ["https://www.enligne.parionssport.fdj.fr/paris-tennis"],
        "Basketball": ["https://www.enligne.parionssport.fdj.fr/paris-basketball"],
        "Badminton": ["https://www.enligne.parionssport.fdj.fr/paris-badminton"],
        "Boxe/MMA": ["https://www.enligne.parionssport.fdj.fr/paris-boxe",
                     "https://www.enligne.parionssport.fdj.fr/paris-ufc-mma"],
        # "Cyclisme": ["https://paris-sportifs.pmu.fr/pari/sport/36/cyclisme"],
        "Golf": ["https://www.enligne.parionssport.fdj.fr/paris-golf"],
        "Handball": ["https://www.enligne.parionssport.fdj.fr/paris-handball"],
        "Hockey": ["https://www.enligne.parionssport.fdj.fr/paris-hockey-sur-glace"],
        "RugbyXV": ["https://www.enligne.parionssport.fdj.fr/paris-rugby"],
        "RugbyXIII": ["https://www.enligne.parionssport.fdj.fr/paris-rugby-a-xiii"],
        "RugbyVII": ["https://www.enligne.parionssport.fdj.fr/paris-rugby-a-7"],
        "Snooker": ["https://www.enligne.parionssport.fdj.fr/paris-snooker"],
        "Volleyball": ["https://www.enligne.parionssport.fdj.fr/paris-volley-ball"],
        "Formule1": ["https://www.enligne.parionssport.fdj.fr/paris-formule-1"],
        "Moto": ["https://www.enligne.parionssport.fdj.fr/paris-moto"],
        "Rallye": ["https://www.enligne.parionssport.fdj.fr/paris-rallye"],
        "Tennis de table": ["https://www.enligne.parionssport.fdj.fr/paris-tennis-de-table"],
        "Baseball": ["https://www.enligne.parionssport.fdj.fr/paris-baseball"],
        "Football Americain": ["https://www.enligne.parionssport.fdj.fr/paris-foot-americain"],
        "Football Australien" : ["https://www.enligne.parionssport.fdj.fr/paris-aussie-rules"],


    }

    def __init__(self):
        self.requestAllCote()

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
            matchSelector = ".psel-sport__event"
            out = htmlToParse.select(matchSelector)
            for match in out:
                nameSelector = ".psel-match__label"
                coteSelector = ".psel-outcome__data"
                matchName = match.select_one(nameSelector).text.replace("/", "-")
                matchCotes = match.select(coteSelector)
                cotes = []
                for rawCote in matchCotes:
                    parsedCote = rawCote.text.replace(" ", "").replace("\n", "").replace(",", '.')
                    if parsedCote != "Accéderaudirect":
                        cotes.append(float(parsedCote))
                if cotes:
                    if matchName not in self.cote[sport]:
                        self.cote[sport][matchName] = cotes
                    else:
                        self.cote[sport]["Duplicate " + matchName] = cotes

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
