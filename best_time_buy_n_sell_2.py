from typing import List


class Solution:
    # Brutal force way to solve the issue
    # the complexity is n^3
    def maxProfit(self, prices: List[int]) -> int:
        """profit:  try every single transaction, then recurse on the remainder."""
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i] + self.maxProfit(prices[j + 1 :])
                    max_profit = max(max_profit, profit)
        return max_profit


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
