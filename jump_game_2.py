from typing import List, Tuple


class Solution:
    def jump(self, nums: List[int]) -> Tuple[int, int, int]:
        return (
            self.jump_greedy_n_elegant(nums),
            self.jump_greedy_n(nums),
            self.jump_greedy_n2(nums),
        )

    def jump_greedy_n_elegant(self, nums: List[int]) -> int:
        # TODO: 2026-07-05 23:50:41
        # This is a solution coming from leetcode solution area
        # I wrote the function below but it was initially very cluncky
        # I wanna know how they differ and why I didn't come up with this solution
        n = len(nums)
        current = 0
        furthest = 0
        jump = 0
        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            if i == current:
                jump += 1
                current = furthest
        return jump

    def jump_greedy_n(self, nums: List[int]) -> int:
        jump_count = 0
        last_furthest = 0
        new_furthest = 0
        if len(nums) == 1:
            return 0
        if last_furthest >= len(nums):
            return 1
        for i in range(len(nums) - 1):
            new_furthest = max(new_furthest, i + nums[i])
            if i == last_furthest:
                jump_count += 1
                last_furthest = new_furthest

        return jump_count

    def jump_greedy_n2(self, nums: List[int]) -> int:
        # time complexity: O(n^2)
        # also it's considering two steps ahead scenario and use greedy to find next step
        jump_count = 0
        pos = 0
        end_pos = len(nums) - 1
        while pos < end_pos:
            if pos + nums[pos] >= end_pos:
                return jump_count + 1
            furtherest = 0
            furtherest_index = 0
            for i in range(pos + 1, pos + nums[pos] + 1):
                if i + nums[i] >= end_pos:
                    return jump_count + 2
                if i + nums[i] > furtherest:
                    furtherest = i + nums[i]
                    furtherest_index = i
            jump_count += 1
            pos = furtherest_index
        return jump_count


nums = [1, 2]
print(Solution().jump(nums))

nums = [2, 3, 1]
print(Solution().jump(nums))

nums = [4, 1, 1, 3, 1, 1, 1]
print(Solution().jump(nums))

nums = [1, 2, 3]
print(Solution().jump(nums))

nums = [1, 1, 1, 1]
print(Solution().jump(nums))

nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
print(Solution().jump(nums))

nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
print(Solution().jump(nums))

nums = [2, 1]
print(Solution().jump(nums))

nums = [1, 2, 0, 1]
print(Solution().jump(nums))
