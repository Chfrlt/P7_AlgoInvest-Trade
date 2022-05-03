import math
from models.base_algo import BaseAlgorithm


class OptimisedAlgorithm(BaseAlgorithm):
    def __init__(self, stocks: list, budget: int,
                 max_nbr_stocks_to_buy: int):
        super().__init__(stocks, budget, max_nbr_stocks_to_buy)
        self.matrix = []

    def set_up_matrix(self):
        self.matrix = (
            [[[0 for _ in range(self.budget + 1)] for
                _ in range(len(self.stocks) + 1)] for
                _ in range(self.max_nbr_stocks_to_buy + 1)]
                )

    def fill_matrix(self) -> None:
        '''
        Go through the matrix indexes and either buy the current stock,
        or skip it, filling up the matrix in the process.
        '''
        for h in range(1, self.max_nbr_stocks_to_buy + 1):
            for i in range(1, len(self.stocks) + 1):
                for j in range(1, self.budget + 1):
                    if (self.stocks[i - 1].price <= j and
                            self.stocks[i - 1].price >= 0):
                        previous_price = math.ceil(self.stocks[i - 1].price)
                        buy = (
                            self.matrix[h - 1][i - 1][j - previous_price]
                            + self.stocks[i - 1].benefit
                            )
                        skip = self.matrix[h][i - 1][j]
                        self.matrix[h][i][j] = max(buy, skip)
                    else:
                        self.matrix[h][i][j] = self.matrix[h][i - 1][j]

    def get_combination(self) -> None:
        '''Function to find the stock combination.
        We start from the matrix box containing the solution, tracing back.

        If there is a benefit difference between a box and the next one,
        the stock was bought.

        Update class parameters to match the solution'''
        curr_combination = []
        i = len(self.stocks)
        h = self.max_nbr_stocks_to_buy
        while i > 0:
            stock = self.stocks[i - 1]
            if (self.matrix[h][i][self.budget] >
                    self.matrix[h][i - 1][self.budget]):
                curr_combination.append(stock)
                self.budget -= math.ceil(stock.price)
                h -= 1
            i -= 1
        self.combination = curr_combination
        self.cost = sum(stock.price for stock in curr_combination)
        self.benefit = sum(stock.benefit for stock in curr_combination)

    def resolve(self):
        self.set_up_matrix()
        self.fill_matrix()
        self.get_combination()
