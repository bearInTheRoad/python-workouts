from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threeSum_twoPointers_skip(nums)

    def threeSum_twoPointers_set(self, nums: list[int]) -> list[list[int]]:

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

    def threeSum_twoPointers_skip(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        i = 0
        possible_solutions = []

        for i in range(len(nums) - 2):
            # if smallest is bigger than 0, then no need
            if nums[i] > 0:
                break

            # skip duplicated i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -1 * nums[i]

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    possible_solutions.append(sorted([nums[i], nums[j], nums[k]]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

                elif nums[j] + nums[k] >= target:
                    k -= 1
                else:
                    j += 1
        return possible_solutions


solution = Solution()
print(solution.threeSum([1, 0, -1, 2, -1, -4]), " ", [[-1, -1, 2], [-1, 0, 1]])
print(solution.threeSum([0, 0, 0]), " ", [0, 0, 0])
print(solution.threeSum([1, 1, -2]), " ", [-2, 1, 1])
