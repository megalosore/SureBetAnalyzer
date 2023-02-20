import requests
from utils import computeCote


class Unibet:
    name = "Unibet"
    websiteUrl = "https://www.unibet.fr/sport"
    sportsUrls = {
        "Football": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=2243762&filter=R%25C3%25A9sultat&marketname=R%25C3%25A9sultat%2520du%2520match",
        "Tennis": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=16883585&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520du%2520match",
        "Basketball": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=991956&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520(Prolongations%2520incluses)",
        "Auto-Moto": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=2741783&filter=Comp%25C3%25A9tition&marketname=Vainqueur%2520-%2520Pilotes",
        "Badminton": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=30485980&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520du%2520match",
        "Baseball": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=264946916&filter=Comp%25C3%25A9tition&marketname=Vainqueur%2520de%2520la%2520comp%25C3%25A9tition",
        "Boxe/MMA": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=6060135&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520du%2520combat",
        "Cyclisme": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=46582804&filter=Comp%25C3%25A9tition&marketname=Vainqueur%2520de%2520la%2520comp%25C3%25A9tition",
        "Football Americain": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=6152799&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520(Prolongations%2520incluses)",
        "Football Australien": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=702556721&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520du%2520match",
        "Golf": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=2116292&filter=Comp%25C3%25A9tition&marketname=Vainqueur%2520de%2520la%2520comp%25C3%25A9tition",
        "Handball": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=11331239&filter=R%25C3%25A9sultat&marketname=R%25C3%25A9sultat%2520du%2520match",
        "Hockey": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=2702713&filter=R%25C3%25A9sultat&marketname=R%25C3%25A9sultat%2520du%2520match",
        "RugbyXV": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=798481&filter=R%25C3%25A9sultat&marketname=R%25C3%25A9sultat%2520du%2520match",
        "RugbyXIII": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=30359680&filter=R%25C3%25A9sultat&marketname=R%25C3%25A9sultat%2520du%2520match",
        "Snooker": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=2692348&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520du%2520match",
        "Hivers": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=675043280&filter=R%25C3%25A9sultat&marketname=Vainqueur",
        "Volleyball": "https://www.unibet.fr/zones/v3/sportnode/markets.json?nodeId=992098&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520du%2520match"
    }
    cote = {}

    def __init__(self):
        self.requestAllCote()

    def requestAllCote(self):
        for sport in self.sportsUrls:
            self.requestCote(sport)

    def __str__(self):
        strReturn = ''
        for sport in self.cote:
            for key, value in self.cote[sport].items():
                strReturn += sport + "| " + key + "| " + str(value) + "\n"
        return strReturn

    def requestCote(self, sport):
        self.cote[sport] = {}  # creating a Category by sport
        url = self.sportsUrls[sport]
        response = requests.get(url)
        data = response.json()
        try:
            DaysList = data["marketsByType"][0]["days"]
        except:
            print(data)
            return
        for day in DaysList:
            for event in day["events"]:  # Tout les match par jour
                cotesList = []
                for outcome in event["markets"][0]["selections"]:
                    cotesList.append(computeCote(outcome["currentPriceUp"], outcome["currentPriceDown"]))
                if event["eventName"] not in self.cote[sport]:
                    self.cote[sport][event["eventName"]] = cotesList
                else:
                    self.cote[sport]["Duplicate "+event["eventName"]] = cotesList

    def getCote(self):
        return self.cote

    def getCoteBySport(self, sport):
        return self.cote[sport]
