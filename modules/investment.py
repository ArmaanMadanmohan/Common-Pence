import random 

class Engine:
    def __init__(self):
        self.stock = Stock()
        self.bonds = 0 
        self.etf = 0 # array of stocks?
        self.bank = Bank()
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
                self.bank.add(value)
            case _:
                raise ValueError(f"Invalid type: {card}")

    def sell(self, card: str, pct: float) -> float:
        total_gained = 0
        match card:
            case "stocks":
                sell_amt = self.stock.shares * pct
                total_gained *= sell_amt * self.stock.share_price 
                self.stock.shares -= sell_amt
            case "bank":
                total_gained = self.bonds * pct
                self.bonds -= total_gained
        self.store -= total_gained
        return total_gained

    def getTotal(self) -> float:
        return self.store
    
    def sellAll(self) -> int:
        self.store = 0
        self.stock.shares = 0
        return self.store

    def tick(self):
        self.stock.update()
        stock_income = self.stock.shares * self.stock.dividend
        self.store += stock_income
        # randomise etf, dividends 
        # fixed coupon (bonds)

class Stock: 
    def __init__(self):
        self.share_price = 4 # random.uniform(3.0, 8.0) 
        self.dividend = self.share_price * random.uniform(0.1, 0.4) # randomise initially
        self.shares = 0

    def add(self, num: int):
        self.shares += num / self.share_price 

    def update(self):   
        growth = random.uniform(-0.1, 0.1)
        self.share_price *= (1 + growth) 
        if growth > 0:
            self.dividend *= (1 + (growth * 0.2))
        elif growth < -0.2:
            self.dividend *= 0.8

class Bank:
    def __init__(self):
        self.interest = 0.03 # random.uniform()?
        self.amt = 0
    
    def add(self, num: int):
        self.amt += num

    def update(self):
        self.amt *= (1 + self.interest)

