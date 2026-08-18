from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        nums = sorted(nums, reverse=True)
        print(nums)

        total = 0
        for i, e in enumerate(nums):
            total += e
            print(i, e, total)
            if total >= target:
                return i + 1

        return 0


nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
solution = Solution()
print(solution.minSubArrayLen(213, nums))
