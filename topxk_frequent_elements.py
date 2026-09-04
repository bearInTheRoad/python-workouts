from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = [0] * (10**5)

        for element in nums:
            counts[element] += 1

        winners = []
        for i in range(k):
            max_num = 0
            max_index = -1
            for index in range(10**5):
                if max_num <= counts[index] and index not in winners:
                    max_num = counts[index]
                    max_index = index
            winners.append(max_index)

        return winners


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
