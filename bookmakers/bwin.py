import requests

idHead = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
clientIdUrl = 'https://sports.bwin.fr/fr/api/clientconfig'
response = requests.get(clientIdUrl, headers=idHead)
accessId = response.json()["msConnection"]["pushAccessId"]

url = "https://cds-api.bwin.fr/bettingoffer/fixtures?x-bwin-accessid=" + accessId + "&lang=fr&country=FR&sportIds=4&take=1000"
response = requests.get(url, headers=idHead)
output = response.json()
for match in output["fixtures"]:
    matchName = match["name"]["value"]
    #matchCotes = 1
