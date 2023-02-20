import random
from bookmakers import *
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from utils import *
import threading
import time

alreadyComputed = set()
alreadyFound = set()
lock = threading.Lock()


def downloadThreading(bookmaker):
    bookmaker.requestAllCote()


# Individual Download Time:
# Unibet: 4.291415691375732
# Winamax: 6.2025532722473145
# Betclic: 8.950401782989502
# Netbet: 10.37904667854309
# Zebet: 14.170216798782349
# Fdj: 20.796252012252808
# Pmu: 25.269271850585938

def computedThreading(bookmaker, bookmakerList):
    global alreadyComputed
    global alreadyFound
    global lock
    for sport in bookmaker.sportsUrls:
        # Shuffle the dict to optimize the usefulness of alreadyComputed
        sportMatches = list(bookmaker.getCoteBySport(sport).items())
        random.shuffle(sportMatches)
        sportMatches = dict(sportMatches)
        for match in sportMatches:
            if match in alreadyComputed:
                continue
            alreadyComputed.add(match)
            cotes = [sportMatches[match]]
            whichBookmaker = [bookmaker.name]
            for bookmakerTarget in bookmakerList:
                if sport in bookmakerTarget.sportsUrls and bookmakerTarget != bookmaker:
                    bookmakerTargetCotes = bookmakerTarget.getCoteBySport(sport)
                    if match not in bookmakerTargetCotes:
                        obtainedCote = getSimilarMatch(match, bookmakerTargetCotes)
                    else:
                        obtainedCote = bookmakerTargetCotes[match]
                    if obtainedCote is not None and len(obtainedCote) == len(cotes[0]):
                        cotes.append(obtainedCote)
                        whichBookmaker.append(bookmakerTarget.name)
            if len(cotes) <= 1:  # No one else know the match
                continue
            bestWager = optimalWager(cotes)
            wagerProfit = arb(bestWager)
            if wagerProfit < 0:
                continue
            nameList = whoseOdd(bestWager, cotes, whichBookmaker)  # List of bookmakers for the bestWager
            idString = str(wagerProfit) + str(bestWager) + str(nameList)  # Unique ID to avoid printing duplicate
            if len(set(nameList)) != 1 and idString not in alreadyFound:
                with lock:
                    print(sport, match, round(arb(bestWager), 2), bestWager, nameList, whoseWebsite(nameList))
                alreadyFound.add(idString)


def main():
    start = time.time()
    global alreadyComputed
    global alreadyFound
    rabona = Rabona()
    betclic = Betclic()
    winamax = Winamax()
    fdj = Fdj()
    netbet = Netbet()
    pmu = Pmu()
    unibet = Unibet()  # 18 requests to Unibet.fr
    zebet = Zebet()
    bookmakerList = (winamax, pmu, unibet, zebet, netbet, fdj, betclic, rabona)
    end = time.time()
    print("Download time: " + str(end - start))
    while True:
        start = time.time()
        with ThreadPoolExecutor(max_workers=12) as compute:
            compute.map(computedThreading, bookmakerList, repeat(bookmakerList))
        end = time.time()
        print(str(end - start) + "-" * 50)
        start = time.time()
        with ThreadPoolExecutor(max_workers=12) as download:
            download.map(downloadThreading, bookmakerList)
        end = time.time()
        print("Threaded download time : " + str(end - start))
        alreadyComputed = set()
        alreadyFound = set()


if __name__ == '__main__':
    main()
