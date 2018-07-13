
class Value:
    def __init__(self):
        pass

    def __lt__(self, other):
        selfDegree, selfRanks = self.getPower()
        otherDegree, otherRanks = other.getPower()

        if selfDegree < otherDegree:
            return True
        elif selfDegree == otherDegree:
            for s,o in zip(selfRanks, otherRanks):
                if s < o:
                    return True
        return False

    def __gt__(self, other):
        selfDegree, selfRanks = self.getPower()
        otherDegree, otherRanks = other.getPower()

        if selfDegree > otherDegree:
            return True
        elif selfDegree == otherDegree:
            for s, o in zip(selfRanks, otherRanks):
                if s > o:
                    return True
        return False

    def getPower(self):
        return [0, []]


class RoyalFlush(Value):
    def __init__(self):
        super().__init__()
        

class StraightFlush(Value):
    def __init__(self, rank):
        super().__init__()
        self.rank = rank

    def getPower(self):
        return [9, []]


class FourOfAKind(Value):
    def __init__(self, quad, kicker):
        super().__init__()
        self.quad = quad
        self.kicker = kicker

    def getPower(self):
        quad = self.quad
        kicker = self.kicker
        return [8, [quad, kicker]]


class FullHouse(Value):
    def __init__(self, full, pair):
        super().__init__()
        self.full = full
        self.pair = pair

    def getPower(self):
        full = self.full
        pair = self.pair
        return [7, [full, pair]]


class Flush(Value):
    def __init__(self, ranks):
        super().__init__()
        self.ranks = ranks

    def getPower(self):
        ranks = self.ranks
        return [6, ranks]


class Straight(Value):
    def __init__(self, rank):
        super().__init__()
        self.rank = rank

    def getPower(self):
        rank = self.rank
        return [5, [rank]]
        

class ThreeOfAKind(Value):
    def __init__(self, trip, kickers):
        super().__init__()
        self.trip = trip
        self.kickers = kickers

    def getPower(self):
        trip = self.trip
        kickers = self.kickers
        return [4, [trip] + kickers]


class TwoPairs(Value):
    def __init__(self, pairs, kicker):
        super().__init__()
        self.pairs = pairs
        self.kicker = kicker

    def getPower(self):
        pairs = self.pairs
        kicker = self.kicker
        return [3, pairs + [kicker]]


class OnePair(Value):
    def __init__(self, pair, kickers):
        super().__init__()
        self.pair = pair
        self.kickers = kickers

    def getPower(self):
        pair = self.pair
        kickers = self.kickers
        return [2, [pair] + kickers]


class HighCard(Value):
    def __init__(self, ranks):
        super().__init__()
        self.ranks = ranks

    def getPower(self):
        ranks = self.ranks
        return [1, ranks]