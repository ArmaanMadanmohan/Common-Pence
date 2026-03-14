import random 

class Engine:
    def __init__(self):
        self.stock = Stock()
        self.bonds = Bond() 
        self.etf = ETF() 
        self.bank = Bank()
        self.store = 0
        self.stage = 0

    def invest(self, card: str, value: int) -> None:  
        match card:   
            case "stocks":
                self.stock.add(value)
            case "bonds":
                self.bonds.add(value, self.stage)
            case "etf":
                self.etf.add(value)
            case "bank":
                self.bank.add(value)
            case _:
                raise ValueError(f"Invalid type: {card}")

    def sell(self, card: str, pct: float) -> float:
        total_gained = 0
        match card:
            case "stocks":
                sell_amt = self.stock.shares * pct
                total_gained = sell_amt * self.stock.share_price 
                self.stock.shares -= sell_amt
            case "bank":
                total_gained = self.bank.amt * pct
                self.bank.amt -= total_gained
            case "bonds":
                total_gained = self.bonds.sell(pct, self.stage)
            case "etf":
                sell_amt = self.etf.shares * pct
                total_gained = sell_amt * self.etf.get_price()
                self.etf.shares -= sell_amt

        # self.store -= total_gained
        return total_gained

    def get_total(self) -> float:
        return self.store
    
    def sell_all(self) -> int:
        self.store = 0
        self.stock.shares = 0
        return self.store

    def tick(self):
        self.stage += 1
        self.stock.update()
        self.etf.update()
        self.bank.update()

        stock_income = self.stock.shares * self.stock.dividend
        etf_income = self.etf.shares * self.etf.get_dividend()
        bond_income = self.bonds.get_coupon_payment() 

        self.store += (stock_income + etf_income + bond_income)

class Stock: 
    def __init__(self):
        self.share_price = 4 # random.uniform(3.0, 8.0) 
        self.dividend = self.share_price * random.uniform(0.1, 0.4) # randomise initially
        self.shares = 0

    def add(self, num: int):
        self.shares += num / self.share_price 

    def update(self, volatility = 1.0):   
        growth = random.uniform(-0.1 * volatility, 0.1 * volatility)
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

class Bond:
    def __init__(self):
        self.coupon_rate = 0.05  
        self.bond_price = 4
        self.contracts = []

    def add(self, amount: int, stage: int):
        new_contract = {
            "principal": amount,
            "due": stage + 4 
        }
        self.contracts.append(new_contract)

    def get_total_principal(self) -> float: 
        return sum(c["principal"] for c in self.contracts)

    def get_coupon_payment(self) -> float:
        return self.get_total_principal() * self.coupon_rate

    def sell(self, pct: float, stage: int) -> float:
        total = 0
        sell_no = int(len(self.contracts) * pct)
        
        # sell matured first
        self.contracts.sort(key=lambda x: x["due"])
        
        to_be_sold = self.contracts[:sell_no]
        self.contracts = self.contracts[sell_no:] 

        for c in to_be_sold:
            principal = c["principal"]

            if stage < c["due"]:
                # penalise per early stage
                penalty_rate = 0.05 * (c["due]"] - stage)
                
                # cap penalty at 80%
                penalty_rate = min(penalty_rate, 0.80)
                
                payout = principal * (1 - penalty_rate)
                total += payout
            else:
                total += principal
            
        return total

class ETF: 
    def __init__(self, size: int = 5): 
        self.holdings = [Stock() for _ in range(size)]
        self.shares = 0

    def get_price(self) -> float:
        total_price = sum(s.share_price for s in self.holdings)
        return total_price / len(self.holdings)

    def get_dividend(self) -> float:
        return sum(s.dividend for s in self.holdings) / len(self.holdings)

    def add(self, cash_amount: int):
        self.shares += cash_amount / self.get_price()

    def update(self):
        for s in self.holdings:
            s.update(0.5)
