from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return self.minSubArrayLen_slidingWindow_myVersion(target, nums)

    def minSubArrayLen_brutefroce(self, target: int, nums: List[int]) -> int:

        for i in range(1, len(nums) + 1):
            j = 0
            while j < len(nums):
                print(nums[j : j + i], sum(nums[j : j + i]))
                if sum(nums[j : j + i]) >= target:
                    return i

                j += 1
        return 0

    def minSubArrayLen_slidingWindow_myVersion(
        self, target: int, nums: List[int]
    ) -> int:
        left = 0
        right = 0

        min_window = 10**5 + 1
        current_sum = sum(nums[left:right])
        decision = "expand"
        while left <= right and right < len(nums) and left < len(nums):
            if decision == "expand":
                current_sum += nums[right]
            else:
                current_sum -= nums[left - 1]
            print(left, right, nums[left : right + 1], current_sum, min_window)
            if current_sum < target:
                # expand the window
                right += 1
                decision = "expand"
            else:
                # shorten the window
                min_window = min(min_window, right - left + 1)
                print(min_window)
                left += 1
                decision = "shrink"

        return min_window if min_window != 10**5 + 1 else 0

    def minSubArrayLen_slidingWindow(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float("inf")

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return int(res) if res != float("inf") else 0


nums = [2, 3, 1, 2, 4, 3]
solution = Solution()
print(solution.minSubArrayLen(7, nums), 2)
nums = [1, 2, 3, 4, 5]
solution = Solution()
print("---------------------")
print(solution.minSubArrayLen(15, nums), 5)

nums = [1, 4, 4]
print("---------------------")
print(solution.minSubArrayLen(4, nums), 1)
