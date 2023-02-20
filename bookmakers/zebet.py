import requests
from bs4 import BeautifulSoup


class Zebet:
    name = "Zebet"
    websiteUrl = "https://www.zebet.fr/fr/sport"
    cote = {}
    sportsUrls = {
        "Football": ["https://www.zebet.fr/fr/sport/13-football"],
        "Tennis": ["https://www.zebet.fr/fr/sport/21-tennis"],
        "Basketball": ["https://www.zebet.fr/fr/sport/4-basketball"],
        "Badminton": ["https://www.zebet.fr/fr/sport/35-badminton"],
        "Boxe/MMA": ["https://www.zebet.fr/fr/sport/23-boxe",
                     "https://www.zebet.fr/fr/sport/78-mma"],
        # "Cyclisme": ["https://paris-sportifs.pmu.fr/pari/sport/36/cyclisme"],
        "Football Americain": ["https://www.zebet.fr/fr/sport/7-foot_us"],
        # "Golf": ["https://paris-sportifs.pmu.fr/pari/sport/4/golf"],
        "Handball": ["https://www.zebet.fr/fr/sport/9-handball"],
        "Hockey": ["https://www.zebet.fr/fr/sport/10-hockey_glace"],
        "RugbyXV": ["https://www.zebet.fr/fr/sport/12-rugby"],
        "RugbyXIII": ["https://www.zebet.fr/fr/sport/38-rugby_a_xiii"],
        "Snooker": ["https://www.zebet.fr/fr/sport/20-snooker"],
        "Volleyball": ["https://www.zebet.fr/fr/sport/14-volleyball"],
        # "Formule1" : ["https://www.zebet.fr/fr/sport/32-formule_1"],
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
            matchSelector = "#sport-top .item-bloc"
            out = htmlToParse.select(matchSelector)
            for match in out:
                nameSelector = ".uk-text-truncate"
                coteSelector = ".pari-1 div div a span.pmq-cote.uk-width-1-1"
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
