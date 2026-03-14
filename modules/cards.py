from modules.cardplay import Card, response_type
from modules.investment import Engine

cards = [
        Card(0, "inv_stocks", response_type.INVEST, Engine),
        Card(1, "inv_ETF", response_type.INVEST, Engine),
        Card(2, "inv_bank", response_type.INVEST, Engine),
        Card(3, "inv_bond", response_type.INVEST, Engine),
        Card(4, "sell_15", response_type.SELL, Engine),
        Card(5, "sell_30", response_type.SELL, Engine),
        Card(6, "sell_50", response_type.SELL, Engine),
        Card(7, "sell_100", response_type.SELL, Engine),
        Card(8, "generate_sm", response_type.INSTANT, Engine),
        Card(9, "generate_lg", response_type.INSTANT, Engine),
        Card(10, "sell_all", response_type.SELL, Engine),
]

