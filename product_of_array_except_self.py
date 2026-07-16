from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums))

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        print(left)
        right = [1] * (len(nums))
        j = len(nums) - 2
        while j >= 0:
            right[j] = right[j + 1] * nums[j + 1]
            j -= 1

        return [i * j for i, j in zip(left, right)]


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
