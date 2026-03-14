from cardplay import Card, response_type
from modules.investment import engine

cards = [
        Card(0, "inv_stocks", response_type.INVEST, engine),
        Card(1, "inv_ETF", response_type.INVEST, engine),
        Card(2, "inv_bank", response_type.INVEST, engine),
        Card(3, "inv_bond", response_type.INVEST, engine),
        Card(4, "sell_15", response_type.SELL, engine),
        Card(5, "sell_30", response_type.SELL, engine),
        Card(6, "sell_50", response_type.SELL, engine),
        Card(7, "sell_100", response_type.SELL, engine),
        Card(8, "generate_sm", response_type.INSTANT, engine),
        Card(9, "generate_lg", response_type.INSTANT, engine),
        Card(10, "sell_all", response_type.SELL, engine),
]

