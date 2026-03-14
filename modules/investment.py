class engine:
    def __init__(self):
        self.stock = 0 # keep track of share count
        self.bonds = 0 # 
        self.etf = 0
        self.bank = 0

    def invest(self, card: str, value: int) -> None:  
        match card:   
            case "stocks":
                self.stock += value
            case "bonds":
                self.bonds += value
            case "etf":
                self.etf += value
            case "bank":
                self.bank += value
            case _:
                raise ValueError(f"Invalid type: {card}")

    # def 

class stock: 
    def __init__(self):
        self.dividend
        self.share_price
        
