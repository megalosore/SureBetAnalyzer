from difflib import SequenceMatcher

import numpy

bookmakersWebsite = {'Fdj': "https://www.enligne.parionssport.fdj.fr/",
                     'Pmu': "https://paris-sportifs.pmu.fr/",
                     "Netbet": "https://www.netbet.fr/",
                     "Unibet": "https://www.unibet.fr/sport",
                     "Winamax": "https://www.winamax.fr/paris-sportifs/sports",
                     "Zebet": "https://www.zebet.fr/fr/sport",
                     "Betclic": "https://www.betclic.fr/",
                     "Rabona": "https://rabona5.com/fr/sport"}


def computeCote(upper, lower):
    """
    Returns the cote computed from integers up and low

    parameters:
        upper (int): upper value used to compute a cote
        lower (int): lower value used to compute a cote

    Returns:
        float: cote
    """
    return round(int(upper) / int(lower) + 1, 2)


def arb(coteList):
    """
    Check if an arbitrage is possible given a list of cote describing all outcomes

    parameter
        coteList (list): List of the cotes of all the outcomes

    Returns
        float: estimated profit in percent
    """
    if not coteList:
        return -999
    arbSum = 0
    for cote in coteList:
        arbSum += 1 / cote
    return (1 - arbSum) * 100


def generateWagers(transposed, wagerList, depth: int):
    """
    Recursive function, can be viewed as traversing an m-ary tree
    Generate all wager possible given the transposed of a matrices of cotes

    parameters:
        transposed (list)(list): transposed of the matrices of cotes
        wagerList (list)(list): Used in the recursion, use [[]] when you call it first
        depth (int): Used in the recursion, use 0 when you call it first

    Returns:
        (list)(list): All possible wagers
    """
    tmpWagerList = []
    for node in transposed[depth]:
        for incomplete in wagerList:
            tmpWagerList.append(incomplete + [node])
    wagerList = tmpWagerList
    if depth + 1 >= len(transposed):
        return wagerList
    else:
        wagerList = generateWagers(transposed, wagerList, depth + 1)
    return wagerList


def optimalWager(cotes):
    transposed = numpy.transpose(cotes)
    return [max(transposed[i]) for i in range(len(transposed))]


def whoseOdd(wager, odds, bookmakers):
    who = []
    for i in range(len(wager)):
        for j in range(len(odds)):
            if wager[i] == odds[j][i]:
                who.append(bookmakers[j])
                break
    return who


def whoseWebsite(nameList):
    webSites = set()
    for bookmaker in nameList:
        if bookmaker in bookmakersWebsite:
            webSites.add(bookmakersWebsite[bookmaker])
        else:
            print(bookmaker)
    return webSites


def getSimilarMatch(reference: str, target):
    """
    Given a list of match, and a reference match name,
    this function return the cote of the most similar match in the target

    parameters:
        reference (str): The reference match name, we search a similar name
        target (list): The list of match name, we search the best fit with reference inside

    Returns:
       list : the cotes of the most similar match to reference
    """
    maximum = [0, '']
    for match in target:
        similarityRatio = similarity(reference, match)
        if similarityRatio > 0.9:
            return target[match]
        elif similarityRatio > maximum[0]:
            maximum[0] = similarityRatio
            maximum[1] = match
    if maximum[0] > 0.85:
        return target[maximum[1]]


def similarity(str1: str, str2: str):
    """
    Simply compute the similarity between two strings
    """
    return SequenceMatcher(None, str1, str2).ratio()
