from enum import Enum

class card_type(Enum):
    INVEST = 1
    SELL = 2
    INSTANT = 3

class invest_type(Enum):
    STOCKS = 1
    ETF = 2
    BONDS = 4
    BANK = 5

class Card:
    def __init__(self, id, name, card_type):
        self.id = id
        self.name = name
        self.card_type = card_type

cards = [
        Card(0, "inv_stocks", card_type.INVEST),
        Card(1, "inv_ETF", card_type.INVEST)
        ]
