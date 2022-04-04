from models.base_algo import BaseAlgorithm


class GreedyAlgorithm(BaseAlgorithm):

    def resolve(self):
        '''
        With x = self.max_nbr_to_buy (int)
        Sort the stocks by ratio, and buy the x best.

        Space complexity : O(N)
        Time complexity : O(N)
        '''
        sorted(self.stocks, reverse=True)
        curr_combination = []
        for i in range(len(self.stocks)):
            curr_cost = sum(stock.price for stock in curr_combination)
            if (curr_cost == self.budget or
                    len(curr_combination) == self.max_nbr_stocks_to_buy):
                break
            elif self.budget - curr_cost - self.stocks[i].price >= 0:
                curr_combination.append(self.stocks[i])
                self.combination = curr_combination
                self.benefit = sum(stock.benefit for stock in curr_combination)
                self.cost = curr_cost
