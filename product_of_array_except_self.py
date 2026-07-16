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

    def productExceptSelfSpaceEfficient(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]

        j = len(nums) - 1
        right = 1
        while j >= 0:
            output[j] = output[j] * right
            right *= nums[j]
            # breakpoint()
            j -= 1

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelfSpaceEfficient([1, 2, 3, 4]))
