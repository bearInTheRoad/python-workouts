from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.canJump_dp(nums)

    # brute force
    # Very easy to understand but bad time complexity
    def canJump_bruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            # if the sum of index i and the value on i
            # is greater or equal to the len of the list
            # then it's true
            if i + nums[i] >= len(nums) - 1:
                return True
            # if all of the sum of index j and the value on j
            # is smaller or equal to the len of range(i, min(i + nums[i], len(nums)))
            # then false
            # if the current value is 0, then we go back and check
            # numbers before current value and see if we can skip to
            # the next number
            if nums[i] == 0 and any(k + nums[k] > i for k in range(0, i)):
                continue
            if all(
                j + nums[j] < min(i + nums[i], len(nums) - 1)
                for j in range(i, min(i + nums[i], len(nums) - 1))
            ):
                return False
        return True

    def canJump_dp(self, nums: List[int]) -> bool:
        # check each element and see where is the furthest they can go
        furtherest = 0
        for i in range(len(nums)):
            if furtherest < i:
                break
            if i + nums[i] >= len(nums) - 1:
                return True
            furtherest = max(furtherest, i + nums[i])
            if furtherest >= len(nums) - 1:
                return True
        return False

    def canJump_gas(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True

    # furthest-reachable greedy with hoisted invariants + direct iteration:
    # O(n) time, O(1) space; keeps the clear invariant of canJump_dp while
    # matching canJump_gas's per-iteration cost (no per-iter len()/max() calls).
    def canJump_dp_fast(self, nums: List[int]) -> bool:
        furthest = 0
        target = len(nums) - 1
        for i, n in enumerate(nums):
            if furthest < i:
                return False
            if i + n > furthest:
                furthest = i + n
            if furthest >= target:
                return True
        return True


nums = [3, 0, 8, 2, 0, 0, 1]
print(Solution().canJump(nums))

nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))

nums = [2, 0, 0, 0]
print(Solution().canJump(nums))

nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))
