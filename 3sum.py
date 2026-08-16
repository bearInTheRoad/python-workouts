from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums = sorted(nums)
        i = 0

        possible_solutions = set()
        while i < len(nums):
            target = -1 * nums[i]
            solution_nums = nums[i + 1 :]

            j = 0
            k = len(solution_nums) - 1
            while j < k:
                if solution_nums[j] + solution_nums[k] == target:
                    possible_solutions.add(
                        tuple(sorted([nums[i], solution_nums[j], solution_nums[k]]))
                    )
                    j += 1
                    k -= 1
                elif solution_nums[j] + solution_nums[k] < target:
                    j += 1
                else:
                    k -= 1

            i += 1

        return list(possible_solutions)


solution = Solution()
print(solution.threeSum([1, 0, -1, 2, -1, -4]), " ", [[-1, -1, 2], [-1, 0, 1]])
