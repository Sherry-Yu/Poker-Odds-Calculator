from scipy import stats

from utility import *
from card import *
from value import *

class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, reverse=True)
        self.ranks = sorted([c.rank.value for c in self.cards], reverse=True)
        self.suits = [c.suit.name for c in self.cards]

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

        isFlush = (len(set(suits)) == 1)
        isStraight = ((ranks == [14,5,4,3,2]) or (diff(ranks) == [1,1,1,1]))

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