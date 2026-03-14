from modules.cardplay import Card, card_type

# We pass None for the engine here, as main.py will dynamically inject the live engine instance
cards = [
        Card(0, "Invest in Stocks", card_type.INVEST, None),
        Card(1, "Invest in ETFs", card_type.INVEST, None),
        Card(2, "Deposit in Bank", card_type.INVEST, None),
        Card(3, "Buy Bonds", card_type.INVEST, None),
        Card(4, "Sell 15% of an Asset", card_type.SELL, None),
        Card(5, "Sell 30% of an Asset", card_type.SELL, None),
        Card(6, "Sell 50% of an Asset", card_type.SELL, None),
        Card(7, "Sell 100% of an Asset", card_type.SELL, None),
        Card(8, "Small Side Hustle (+£25)", card_type.INSTANT, None),
        Card(9, "Large Side Hustle (+£50)", card_type.INSTANT, None),
        Card(10, "Liquidate Everything (Sell All)", card_type.SELL, None),
]
