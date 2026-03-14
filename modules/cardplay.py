from enum import Enum
from modules.investment import Engine

class card_type(Enum):
    INVEST = 1
    SELL = 2
    INSTANT = 3

class response_type(Enum):
    INVEST = 1
    SELL = 2
    INSTANT = 3
    ERROR = 4

class Response:
    def __init__(self, response_type: response_type, text: str):
        self.response_type = response_type
        self.text = text

class Card:
    def __init__(self, id, name, card_type, engine):
        self.id = id
        self.name = name
        self.card_type = card_type
        self.engine = engine

    def play_card(self):
        if self.card_type == card_type.INVEST:
            self.play_invest()

        if self.play_card == card_type.SELL:
            self.play_sell()

        if self.play_card == card_type.INSTANT:
            self.play_instant()

    def play_invest(self) -> Response:
        value = int(input("Select an amount of money to invest\n"))
        if self.id == 0:
            self.engine.invest("stocks", value)
            return Response(response_type.INVEST, f"Invested {value} in stocks")

        elif self.id == 1:
            self.engine.invest("etf", value)
            return Response(response_type.INVEST, f"Invested {value} in etf")

        elif self.id == 2:
            self.engine.invest("bank", value)
            return Response(response_type.INVEST, f"Invested {value} in bank")

        elif self.id == 3:
            self.engine.invest("bond", value)
            return Response(response_type.INVEST, f"Invested {value} in bond")

        return Response(response_type.ERROR, "Failed")

    def play_sell(self) -> Response:
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

        if self.id == 4:
            res = engine.sell(15, inv)
            return Response(response_type.SELL, res)

        if self.id == 5:
            res = engine.sell(30, inv)
            return Response(response_type.SELL, res)

        if self.id == 6:
            res = engine.sell(50, inv)
            return Response(response_type.SELL, res)

        if self.id == 7:
            res = engine.sell(100, inv)
            return Response(response_type.SELL, res)

        if self.id == 10:
            res = engine.sellall()
            return Response(response_type.SELL, res)

        return Response(response_type.ERROR, "Failed")

    def play_instant(self) -> Response:
        if self.id == 8:
            return Response(response_type.INSTANT, "25")

        if self.id == 9: 
            return Response(response_type.INSTANT, "50")

        return Response(response_type.ERROR, "Failed")

