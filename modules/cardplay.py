from enum import Enum

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
    def __init__(self, response_type: response_type, text: str, value: float = 0):
        self.response_type = response_type
        self.text = text
        self.value = value

class Card:
    def __init__(self, id, name, c_type, engine):
        self.id = id
        self.name = name
        self.card_type = c_type
        self.engine = engine

    def play_card(self, player_cash: float) -> Response:
        if self.card_type == card_type.INVEST:
            return self.play_invest(player_cash)
        elif self.card_type == card_type.SELL:
            return self.play_sell()
        elif self.card_type == card_type.INSTANT:
            return self.play_instant()
            
        return Response(response_type.ERROR, "Unknown card type", 0)

    def play_invest(self, player_cash: float) -> Response:
        try:
            value = float(input(f"Select an amount of money to invest (Max available: £{player_cash:.2f})\n£"))
        except ValueError:
            return Response(response_type.ERROR, "Invalid amount.", 0)

        if value <= 0 or value > player_cash:
            return Response(response_type.ERROR, "Invalid investment amount. Not enough cash.", 0)

        if self.id == 0:
            self.engine.invest("stocks", value)
            return Response(response_type.INVEST, f"Invested £{value} in stocks", value)
        elif self.id == 1:
            self.engine.invest("etf", value)
            return Response(response_type.INVEST, f"Invested £{value} in etf", value)
        elif self.id == 2:
            self.engine.invest("bank", value)
            return Response(response_type.INVEST, f"Invested £{value} in bank", value)
        elif self.id == 3:
            self.engine.invest("bond", value)
            return Response(response_type.INVEST, f"Invested £{value} in bond", value)

        return Response(response_type.ERROR, "Failed", 0)

    def play_sell(self) -> Response:
        try:
            investment_to_sell = int(input("""
Select an investment to sell:
1. stocks
2. etf
3. bank
4. bond
Choice: """))
        except ValueError:
            return Response(response_type.ERROR, "Invalid choice", 0)

        inv = ""
        match investment_to_sell:
            case 1: inv = "stocks"
            case 2: inv = "etf"
            case 3: inv = "bank"
            case 4: inv = "bond"
            case _: return Response(response_type.ERROR, "Invalid option.", 0)

        if self.id == 4:
            res = self.engine.sell(inv, 0.15)
            return Response(response_type.SELL, f"Sold 15% of {inv} for £{res:.2f}", res)
        elif self.id == 5:
            res = self.engine.sell(inv, 0.30)
            return Response(response_type.SELL, f"Sold 30% of {inv} for £{res:.2f}", res)
        elif self.id == 6:
            res = self.engine.sell(inv, 0.50)
            return Response(response_type.SELL, f"Sold 50% of {inv} for £{res:.2f}", res)
        elif self.id == 7:
            res = self.engine.sell(inv, 1.00)
            return Response(response_type.SELL, f"Sold 100% of {inv} for £{res:.2f}", res)
        elif self.id == 10:
            res = self.engine.sellAll()
            return Response(response_type.SELL, f"Sold ALL investments for £{res:.2f}", res)

        return Response(response_type.ERROR, "Failed", 0)

    def play_instant(self) -> Response:
        if self.id == 8:
            return Response(response_type.INSTANT, "Gained £25 from side hustle!", 25)
        if self.id == 9: 
            return Response(response_type.INSTANT, "Gained £50 from side hustle!", 50)

        return Response(response_type.ERROR, "Failed", 0)
