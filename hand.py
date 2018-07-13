import numpy as np
from scipy import stats
from value import *

class Rank:
    def __init__(self, name):
        self.name = str(name)
        if name == 'A':
            self.value = 14
        elif name == 'K':
            self.value = 13
        elif name == 'Q':
            self.value = 12
        elif name == 'J':
            self.value = 11
        elif name == 'T':
            self.value = 10
        else:
            self.value = int(name)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


class Suit:
    def __init__(self, name):
        if name == 'S' or name == 'Spade':
            self.name = 'Spade'
        elif name == 'H' or name == 'Heart':
            self.name = 'Heart'
        elif name == 'C' or name == 'Club':
            self.name = 'Club'
        elif name == 'D' or name == 'Diamond':
            self.name = 'Diamond'


class Card:
    def __init__(self, rank, suit):
        self.rank = Rank(rank)
        self.suit = Suit(suit)

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Hand:
    def __init__(self, cards):
        self.cards = np.sort(cards)
        self.ranks = np.array([c.rank.value for c in self.cards])
        self.suits = np.array([c.suit.name for c in self.cards])

    def __eq__(self, other):
        selfValue = self.getValue()
        otherValue = other.getValue()
        return selfValue == otherValue

    def __lt__(self, other):
        selfValue = self.getValue()
        otherValue = other.getValue()
        return selfValue < otherValue

    def __gt__(self, other):
        selfValue = self.getValue()
        otherValue = other.getValue()
        return selfValue > otherValue

    def getValue(self):
        ranks = self.ranks
        suits = self.suits

        isFlush = (suits.unique().shape[0] == 1)
        isStraight = ((ranks == np.array([2,3,4,5,14])) or (ranks.diff() == np.array([1,1,1,1])))

        rankDict = {k:v for k,v in stats.itemfreq(ranks)}
        length = len(rankDict)
        maxKey = max(rankDict)
        maxValue = rankDict[maxKey]

        isQuad = ((length == 2) and (maxValue == 4))
        isFull = ((length == 2) and (maxValue == 3))
        isSet = ((length == 3) and (maxValue == 3))
        isTwo = ((length == 3) and (maxValue == 2))
        isOne = ((length == 4) and (maxValue == 2))

        if isFlush and isStraight:
            rank = ranks[-1]
            if rank == 14:
                return RoyalFlush()
            else:
                return StraightFlush(rank)

        elif isFlush:
            return Flush(ranks)
        elif isStraight:
            rank = ranks[-1]
            return Straight(rank)

        elif isQuad:
            quad = max(rankDict)
            kicker = min(rankDict)
            return FourOfAKind(quad, kicker)
        elif isFull:
            full = max(rankDict)
            pair = min(rankDict)
            return FullHouse(full, pair)

        elif isSet:
            trip = max(rankDict)
            kickers = sorted([k for k,v in rankDict.items() if v == 1], reverse=True)
            return ThreeOfAKind(trip, kickers)
        elif isTwo:
            pairs = sorted([k for k,v in rankDict.items() if v == 2], reverse=True)
            kicker = min(rankDict)
            return TwoPairs(pairs, kicker)
        elif isOne:
            pair = max(rankDict)
            kickers = sorted([k for k,v in rankDict.items() if v == 1], reverse=True)
            return OnePair(pair, kickers)

        else:
            ranks = sorted([k for k,v in rankDict.items() if v == 1], reverse=True)
            return HighCard(ranks)