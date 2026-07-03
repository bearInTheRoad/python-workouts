from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # let's try greedy first
        # this will fail at places like [4, 1, 1, 3, 1, 1, 1]
        # becasue we didn't consider the ones in the middle
        #
        #
        # We should find a way to scan the whole jumpable range
        # then see where is the furtherest you can jump
        #
        # may be we should consider 2 steps forward instead of 1
        # still using greedy
        # jump_count = 0
        # pos = 0
        # end_pos = len(nums) - 1
        # while pos < end_pos:
        #     if pos + nums[pos] >= end_pos:
        #         return jump_count + 1
        #     if nums[pos] < nums[pos + 1]:
        #         jump_count += 1
        #         pos += 1
        #     else:
        #         jump_count += 1
        #         pos += nums[pos]
        # return jump_count

        jump_count = 0
        pos = 0
        end_pos = len(nums) - 1
        while pos < end_pos:
            if pos + nums[pos] >= end_pos:
                return jump_count + 1
            if any(i + nums[i] >= end_pos for i in range(pos, pos + nums[pos] + 1)):
                return jump_count + 2
            pos = max(i + nums[i] for i in range(pos, pos + nums[pos]))
            jump_count += 2
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
