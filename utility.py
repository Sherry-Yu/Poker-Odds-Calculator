from card import *


def diff(array):
    head = array[:-1]
    tail = array[1:]
    return [h-t for h,t in zip(head,tail)]

def cardToIndex(card):
    rankDict = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
    suitDict = {'Spade':0, 'Heart':1, 'Club':2, 'Diamond':3}

    rankName = card.rank.name
    suitName = card.suit.name

    return rankDict[rankName] + suitDict[suitName] * 13

def indexToCard(index):
    rankDict = {1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'T', 11:'J', 12:'Q', 13:'K'}
    suitDict = {0:'Spade', 1:'Heart', 2:'Club', 3:'Diamond'}

    suitIndex = int((index - 1) / 13)
    rankIndex = index - suitIndex * 13

    return Card(rankDict[rankIndex], suitDict[suitIndex])