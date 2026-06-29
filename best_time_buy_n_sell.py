from typing import List, Tuple


class Solution:
    # def linearFind(self, prices: List[int]) -> Tuple[int, int, int]:
    #     min_price_index = 0
    #     for i in range(len(prices)):
    #         if prices[i] <= prices[min_price_index]:
    #             min_price_index = i
    #
    #     print(min_price_index)
    #     max_price_index = min_price_index
    #     for i in range(min_price_index, len(prices)):
    #         if prices[i] >= prices[max_price_index]:
    #             max_price_index = i
    #
    #     print(max_price_index)
    #     profit = prices[max_price_index] - prices[min_price_index]
    #     return (profit if profit > 0 else 0, min_price_index, max_price_index)
    #
    #
    # def maxProfit(self, prices: List[int]) -> int:
    #     profit, min_price_index, max_price_index = self.linearFind(prices)
    #     if min_price_index < max_price_index:
    #         return profit
    #     else:
    #         profit_left, _, _ = self.linearFind(prices[:min_price_index])
    #         profit_right, _, _ = self.linearFind(prices[min_price_index:])
    #         return max(profit_left, profit_right)

    # n^2 brutal force, can't pass test when the n is large
    # works but the time limit exceeds in later test cases
    # def maxProfit(self, prices: List[int]) -> int:
    #     max_profit = 0
    #     for i in range(len(prices)):
    #         buy_price = prices[i]
    #         for sell_price in prices[i + 1 :]:
    #             if sell_price - buy_price > max_profit:
    #                 max_profit = sell_price - buy_price
    #     return max_profit

    # divide and conquer
    # this past the time limit, but still very slow
    # the only good part is that it optimize the best case compared
    # to brutal force
    # def findMaxMinIndex(
    #     self, prices: List[int], start: int, end: int
    # ) -> Tuple[int, int]:
    #
    #     min_price_index = min(range(start, end), key=prices.__getitem__)
    #     max_price_index = max(range(start, end), key=prices.__getitem__)
    #     return max_price_index, min_price_index
    #
    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) < 2:
    #         return 0
    #     max_price_index, min_price_index = self.findMaxMinIndex(prices, 0, len(prices))
    #     print(max_price_index, min_price_index)
    #
    #     if max_price_index >= min_price_index:
    #         return prices[max_price_index] - prices[min_price_index]
    #
    #     else:
    #         max_profit_left = self.maxProfit(prices[0 : max_price_index + 1])
    #         max_profit_middle = self.maxProfit(
    #             prices[max_price_index + 1 : min_price_index]
    #         )
    #         max_profit_right = self.maxProfit(prices[min_price_index:])
    #
    #         return max(max_profit_left, max_profit_middle, max_profit_right)

    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

            # print("max profit ", max_profit)
            # print("min_price ", min_price)

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print("max profit is ", solution.maxProfit(prices))

prices = [2, 4, 1]
solution = Solution()
print("max profit is ", solution.maxProfit(prices))
