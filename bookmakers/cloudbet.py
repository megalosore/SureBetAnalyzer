import requests

url = 'https://www.cloudbet.com/sports-api/c/v6/sports/events?limit=10000'

response = requests.get(url)
data = response.json()
competitionsList = data['sports'][2]['competitions']
for competition in competitionsList:
    for match in competition['events']:
        print(match['name'])
