class BaseAlgorithm:
    def __init__(self, stocks: list,
                 budget: int,
                 max_nbr_stocks_to_buy: int):
        self.max_nbr_stocks_to_buy = max_nbr_stocks_to_buy
        self.budget = budget
        self.stocks = stocks
        self.nbr_stocks = len(stocks)
        self.combination = []
        self.benefit = 0
        self.cost = 0

    def __repr__(self) -> str:
        return "Purchased: {}\nTotal benefit: {}\nCost: {}".format(
            self.combination, self.benefit, self.cost)
