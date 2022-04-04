from models.base_algo import BaseAlgorithm


class BruteForceAlgorithm(BaseAlgorithm):

    def resolve(self):
        '''
        Nbr of possible combinations is 2^N.

        Go through the list of stocks, and using a binary representation,
        check if current stock is in it.

        Update class parameters to match the best possible combination in terms of
        benefit.

        Space complexity: O(2^N)
        Time complexity : O(2^N)
        '''
        nbr_possible_combination = 2 ** len(self.stocks)
        for i in range(nbr_possible_combination):
            curr_combination = []
            for j in range(len(self.stocks)):
                if (i >> j) % 2 == 1:
                    curr_combination.append(self.stocks[j])
            curr_price = sum(stock.price for stock in curr_combination)
            curr_benefit = sum(stock.benefit for stock in curr_combination)
            if (self.budget - curr_price >= 0 and
                    len(curr_combination) <= self.max_nbr_stocks_to_buy and
                    curr_benefit > self.benefit):
                self.combination = curr_combination
                self.benefit = curr_benefit
                self.cost = curr_price
