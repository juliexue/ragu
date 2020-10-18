from enum import Enum


class Suit(Enum):
    DIAMOND = 'D'
    CLUB = 'C'
    HEART = 'H'
    SPADE = 'S'
    JOKER = 'J'


class Card(object):
    def __init__(self, rank: int, suit: Suit, is_trump: bool):
        self.rank = rank
        self.suit = suit
        self.is_trump = is_trump
