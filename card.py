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