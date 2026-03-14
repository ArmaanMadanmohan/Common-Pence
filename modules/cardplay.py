from enum import Enum
from investment import engine

class card_type(Enum):
    INVEST = 1
    SELL = 2
    INSTANT = 3

class Card:
    def __init__(self, id, name, card_type, engine):
        self.id = id
        self.name = name
        self.card_type = card_type
        self.engine = engine

    def play_card(self):
        print("playing")
        if self.card_type == card_type.INVEST:
            self.play_invest()

        if self.play_card == card_type.SELL:
            self.play_sell()

        if self.play_card == card_type.INSTANT:
            self.play_instant()

    def play_invest(self):
        value = int(input("Select an amount of money to invest\n"))
        if self.id == 0:
            self.engine.invest("stocks", value)

        elif self.id == 1:
            self.engine.invest("etf", value)

        elif self.id == 2:
            self.engine.invest("bank", value)

        elif self.id == 3:
            self.engine.invest("bond", value)

    def play_sell(self):
        investment_to_sell = str(input("""
                                       Select an investment to sell:
                                       1. stocks
                                       2. etf
                                       3. bank
                                       4. bond
                                       """))

        inv = ""
        match investment_to_sell:
            case 1: inv = "stocks"
            case 2: inv = "etf"
            case 3: inv = "bank"
            case 4: inv = "bond"

        # if self.id == 4: // sell 15
        #     engine.sell(15, inv)
        #
        # if self.id == 5: // sell 30
        #     engine.sell(30, inv)
        #
        # if self.id == 6: // sell 50
        #     engine.sell(50, inv)
        #
        # if self.id == 7: // sell 100
        #     engine.sell(100, inv)

    def play_instant(self):
        if self.id == 8:
            pass

        if self.id == 9: 
            pass


cards = [
        Card(0, "inv_stocks", card_type.INVEST, engine),
        Card(1, "inv_ETF", card_type.INVEST, engine),
        Card(2, "inv_bank", card_type.INVEST, engine),
        Card(3, "inv_bond", card_type.INVEST, engine),
        Card(4, "sell_15", card_type.SELL, engine),
        Card(5, "sell_30", card_type.SELL, engine),
        Card(6, "sell_50", card_type.SELL, engine),
        Card(7, "sell_100", card_type.SELL, engine),
        Card(8, "generate_sm", card_type.INSTANT, engine),
        Card(9, "generate_lg", card_type.INSTANT, engine),
]

