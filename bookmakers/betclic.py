import requests


class Betclic:
    sportsUrls = {
        "Football": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=1"],
        "Tennis": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=2"],
        "Basketball": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=4"],
        "Boxe/MMA": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=16",
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=23"],
        "Badminton": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=27"],
        "Cyclisme": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=6"],
        "Football Americain": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=14"],
        "Football Australien": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=73"],
        "Golf": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=7"],
        "Handball": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=9"],
        "Hockey": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=13"],
        "RugbyXV": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=5"],
        "RugbyXIII": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=52"],
        "Snooker": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=54"],
        "Volleyball": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=8"],
        "Formule1": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=3"],
        "Baseball": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=20"],
        "Biathlon": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=62"],
        "Moto": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=15"],
        "Nascar": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=24"],
        "Rallye": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=19"],
        "Hivers": [
            "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=18"],

    }
    websiteUrl = "https://www.betclic.fr/"
    name = "Betclic"
    cote = {}

    def __init__(self):
        self.requestAllCote()

    def requestAllCote(self):
        for sport in self.sportsUrls:
            self.requestCote(sport)

    def requestCote(self, sport):
        req = requests.Session()
        head = {
            'Host': 'offer.cdn.begmedia.com',
            'Content-Length': '0',
            'Origin': 'https://www.betclic.fr/',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.betclic.fr',
            'Cookie': 'sticky=balancer.wsnb5; nb-ipclient=2a02:6ea0:dc05::a15e',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
            'Accept': 'application/json',
        }
        self.cote[sport] = {}
        urlList = self.sportsUrls[sport]
        for url in urlList:
            response = req.get(url, headers=head)
            data = response.json()
            for match in data:
                matchName = match["name"]
                if 'markets' not in match or not match["markets"]:
                    continue
                marketOddList = match["markets"][0]["selections"]
                cotes = []
                for odds in marketOddList:
                    cotes.append(odds["odds"])
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
