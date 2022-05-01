from typing import Union

from models.base_algo import BaseAlgorithm


class Recursive(BaseAlgorithm):
    '''
    Simple recursive method.
    '''

    def resolve(self, stock_index: int = None,
                curr_budget: Union[int, float] = None,
                curr_combination: list = None):
        if curr_combination is None:
            curr_combination = []
        if stock_index is None:
            stock_index = len(self.stocks)
        if curr_budget is None:
            curr_budget = self.budget

        if (stock_index == 0 or
                curr_budget == 0 or
                len(curr_combination) > self.max_nbr_stocks_to_buy):
            return [], 0

        if self.stocks[stock_index - 1].price > curr_budget:
            return self.resolve(stock_index - 1, curr_budget)

        curr_combination, curr_benefit = (
            self.resolve(stock_index - 1,
                         curr_budget - self.stocks[stock_index - 1].price)
                         )
        curr_combination.append(self.stocks[stock_index - 1])
        curr_benefit += self.stocks[stock_index - 1].benefit
        self.combination, self.benefit = (
            self.resolve(stock_index - 1, curr_budget))
        if self.benefit < curr_benefit:
            self.benefit = curr_benefit
            self.combination = curr_combination
            self.cost = sum(stock.price for stock in curr_combination)
        return ((curr_combination, curr_benefit) if
                curr_benefit > self.benefit else
                (self.combination, self.benefit))
