import requests
import re
import json


def checkBetType(betId, jsonData):
    filterList = [1, 2, 12, 106, 112, 133, 151, 158, 178, 205, 212, 213, 245, 252, 253, 276, 284, 332, 338, 339,
                  362, 368, 369, 396, 404, None]
    if betId is not None and str(betId) in jsonData["bets"]:
        return jsonData["bets"][str(betId)]["betTypeCategoryId"] in filterList
    else:
        return False


def extractBet(betType, jsonData, betIdList):
    for betId in betIdList:
        if checkBetType(betId, jsonData) == betType:
            return betId


class Winamax:
    name = "Winamax"
    websiteUrl = "https://www.winamax.fr/paris-sportifs/sports"
    sportsUrls = {
        "Football": "https://www.winamax.fr/paris-sportifs/sports/1",
        "Tennis": "https://www.winamax.fr/paris-sportifs/sports/5",
        "Basketball": "https://www.winamax.fr/paris-sportifs/sports/2",
        "Auto-Moto": "https://www.winamax.fr/paris-sportifs/sports/11",
        "Badminton": "https://www.winamax.fr/paris-sportifs/sports/31",
        "Baseball": "https://www.winamax.fr/paris-sportifs/sports/3",
        "Boxe/MMA": "https://www.winamax.fr/paris-sportifs/sports/117",
        "Cyclisme": "https://www.winamax.fr/paris-sportifs/sports/17",
        "Football Americain": "https://www.winamax.fr/paris-sportifs/sports/16",
        "Football Australien": "https://www.winamax.fr/paris-sportifs/sports/13",
        "Formule1": "https://www.winamax.fr/paris-sportifs/sports/13",
        "Golf": "https://www.winamax.fr/paris-sportifs/sports/9",
        "Handball": "https://www.winamax.fr/paris-sportifs/sports/6",
        "Hockey": "https://www.winamax.fr/paris-sportifs/sports/4",
        "RugbyXV": "https://www.winamax.fr/paris-sportifs/sports/12",
        "RugbyXIII": "https://www.winamax.fr/paris-sportifs/sports/9992",
        "Snooker": "https://www.winamax.fr/paris-sportifs/sports/19",
        "Hivers": "https://www.winamax.fr/paris-sportifs/sports/14",
        "Volleyball": "https://www.winamax.fr/paris-sportifs/sports/23"
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

    def requestData(self, sport):
        url = self.sportsUrls[sport]
        head = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 9; ASUS_X00TD; Flow) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/359.0.0.288 Mobile Safari/537.36"}
        response = requests.get(url, headers=head)
        regex = re.compile('{"sportIds.*;</script><script t')  # Regex to get the Json data
        regexOutput = regex.search(response.text)
        isolatedData = regexOutput.group().rstrip(";</script><script t")
        jsonData = json.loads(isolatedData)
        return jsonData

    def requestCote(self, sport):
        self.cote[sport] = {}  # Creating the sport category / Emptying it
        jsonData = self.requestData(sport)
        for matchId in jsonData["matches"]:
            coteList = []
            match = jsonData["matches"][matchId]
            betId = match["mainBetId"]
            if not checkBetType(betId, jsonData):  # Check if the wager  represent a match result
                # print(matchId)
                continue
            if str(betId) in jsonData[
                "bets"]:  # and 'img' not in match: Strange match are added where they should not be, but it's not that much of a problem
                for outcomeId in jsonData["bets"][str(betId)]["outcomes"]:
                    coteList.append(jsonData["odds"][str(outcomeId)])
                if match["title"] not in self.cote[sport]:
                    self.cote[sport][match["title"]] = coteList
                else:
                    self.cote[sport]["Duplicate " + match["title"]] = coteList

    def getCote(self):
        return self.cote

    def getCoteBySport(self, sport):
        return self.cote[sport]
