import random 

class Engine:
    def __init__(self):
        self.stock = Stock()
        self.bonds = 0 
        self.etf = 0 # array of stocks?
        self.bank = 0
        self.store = 0

    def invest(self, card: str, value: int) -> None:  
        match card:   
            case "stocks":
                self.stock.add(value)
            case "bonds":
                self.bonds += value
            case "etf":
                self.etf += value
            case "bank":
                self.bank += value
            case _:
                raise ValueError(f"Invalid type: {card}")

    def sell(self, card: str, pct: float) -> int:
        total_gained = 0
        match card:
            case "stocks":
                sell_amt = self.stock.shares * pct
                total_gained *= sell_amt * self.stock.share_price 
                self.stock.shares -= sell_amt
            case "bonds":
                total_gained = self.bonds * pct
                # self.bonds -= total_gained
        self.store -= total_gained
        return total_gained

    def getTotal(self) -> int:
        return self.store
    
    def sellAll(self) -> int:
        self.store = 0
        self.stock.shares = 0
        return self.store

    def tick(self):
        self.stock.update()
        # randomise etf, dividends 
        # fixed coupon (bonds)

class Stock: 
    def __init__(self):
        self.dividend = 0 # randomise initially
        self.share_price = 0 # randomise initially and growth and multiply share price by that
        self.shares = 0

    def add(self, num: int):
        self.shares += num
        self.shares = num / self.share_price 

    def update(self):   
        growth = random.uniform(-0.1, 0.1)
        self.share_price *= (1 + growth) 
        if growth > 0:
            self.dividend *= (1 + (growth * 0.2))
        elif growth < -0.2:
            self.dividend *= 0.8

class Bond:
    def __init__(self):
        self.interest = 0
        self.amt = 0
    
    def add(self, num: int):
        self.amt += num

    # def update(self):

