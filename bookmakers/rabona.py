import requests


class Rabona:
    name = "Rabona"
    cote = {}
    sportsUrls = {
        "Football": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=66&count=10000&langId=39"],
        "Tennis": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=68&count=10000&langId=39"],
        "Basketball": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=67&count=10000&langId=39"],
        "Tennis de table": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=77&count=10000&langId=39"],
        "Boxe/MMA": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=84&count=10000&langId=39",
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=71&count=10000&langId=39"],
        "Badminton": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=72&count=10000&langId=39"],
        "Cyclisme": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=89&count=10000&langId=39"],
        "Football Americain": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=75&count=10000&langId=39"],
        "Football Australien": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=73&count=10000&langId=39"],
        "Golf": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=85&count=10000&langId=39"],
        "Handball": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=73&count=10000&langId=39"],
        "Hockey": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=70&count=10000&langId=39"],
        "RugbyXV": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=102&count=10000&langId=39"],
        "RugbyXIII": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=101&count=10000&langId=39"],
        "Snooker": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=81&count=10000&langId=39"],
        "Volleyball": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=69&count=&langId=39"],
        "Baseball": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=76&count=10000&langId=39"],
        "Biathlon": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=93&count=10000&langId=39"],
        "Auto-Moto": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=103&count=10000&langId=39"],
        "Flechettes": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=78&count=10000&langId=39"],
        "Hivers": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=91&count=10000&langId=39"],
        "Waterpolo": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=83&count=10000&langId=39"],
        "Cricket": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=149&count=10000&langId=39"],
        "Boules": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=108&count=10000&langId=39"],
        "E-Sport": [
            "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?skinName=rabona&configId=12&integration=rabona&sportId=145&count=10000&langId=39"]

    }

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
        req = requests.Session()
        head = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        }
        self.cote[sport] = {}
        urlList = self.sportsUrls[sport]
        for url in urlList:
            response = req.get(url, headers=head)
            try:
                data = response.json()["Result"]["Items"][0]
            except:
                continue
            for match in data["Events"]:
                matchName = match["Name"]
                if 'Items' not in match or not match["Items"]:
                    continue
                marketOddList = match["Items"][0]["Items"]
                cotes = []
                for odds in marketOddList:
                    cotes.append(odds["Price"])
                if matchName not in self.cote[sport]:
                    self.cote[sport][matchName] = cotes
                else:
                    self.cote[sport]["Duplicate " + matchName] = cotes

    def getCote(self):
        return self.cote

    def getCoteBySport(self, sport):
        return self.cote[sport]