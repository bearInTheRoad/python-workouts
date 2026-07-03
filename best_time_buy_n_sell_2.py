from typing import List
from functools import lru_cache


class Solution:
    # Brutal force way to solve the issue
    # the complexity is n^3
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfit_realLruRecusion(tuple(prices))  # list -> tuple (hashable)

    def maxProfit_naiveRecursion(self, prices: List[int]) -> int:
        """profit:  try every single transaction, then recurse on the remainder."""
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i] + self.maxProfit(prices[j + 1 :])
                    max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit_cheatFast(self, prices: List[int]) -> int:
        """profit: just go with the vibe - daily profit accumualted up will be the"""
        """same as the best profit at the end of the day."""
        max_profit = 0
        buy_price = prices[0]
        for i in range(len(prices)):
            if prices[i] > buy_price:
                max_profit += prices[i] - buy_price
            buy_price = prices[i]
        return max_profit

    @lru_cache(maxsize=None)
    def maxProfit_naiveLruRecusion(self, prices: tuple) -> int:
        """Same implementation as maxProfit_naiveRecursion, but with lru_cache.

        Two fixes vs the broken version:
        - prices is a tuple (hashable), so lru_cache can key on it.
        - recursion calls *itself*, not the public wrapper, so the cache is used.
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = (
                        prices[j]
                        - prices[i]
                        + self.maxProfit_naiveLruRecusion(prices[j + 1 :])
                    )
                    max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit_realLruRecusion(self, prices: tuple) -> int:
        # We use a helper function so we can pass integer indices,
        # which are tiny, fast, and highly cacheable.
        @lru_cache(maxsize=None)
        def solve(i: int, holding: bool) -> int:
            # Base Case: Out of days, no more profit can be made
            if i >= len(prices):
                return 0

            if holding:
                # Choice 1: Sell today -> get prices[i] cash + move to next day (holding=False)
                # Choice 2: Hold -> skip today + move to next day (holding=True)
                sell = prices[i] + solve(i + 1, False)
                hold = solve(i + 1, True)
                return max(sell, hold)
            else:
                # Choice 1: Buy today -> spend prices[i] cash + move to next day (holding=True)
                # Choice 2: Skip today -> move to next day (holding=False)
                buy = -1 * prices[i] + solve(i + 1, True)
                skip = solve(i + 1, False)
                return max(buy, skip)

        # Start on Day 0, not holding any stock
        return solve(0, False)


prices = [7, 1, 5, 3, 6, 4]
print(
    "profit: ",
    Solution().maxProfit(prices),
)  # expected 7

prices = [7, 6, 4, 3, 1]
print(
    "profit: ",
    Solution().maxProfit(prices),
)  # expected 0

prices = [1, 2, 3, 4, 5]
print(
    "profit: ",
    Solution().maxProfit(prices),
)  # expected 4

prices = [1, 2, 3]
print(
    "profit: ",
    Solution().maxProfit(prices),
)  # expected 2
