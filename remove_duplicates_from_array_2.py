from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mem_num = nums[0]
        num_counter = 0
        scout_ptr = 0
        build_ptr = 0

        while scout_ptr < len(nums):
            # print("BEFORE")
            # print("build_ptr ", build_ptr)
            # print("mem_num ", mem_num)
            # print("num_counter ", num_counter)
            # print("scout_ptr ", scout_ptr)
            # print("nums ", nums)
            # print("-----------------")
            while scout_ptr < len(nums) and nums[scout_ptr] == mem_num:
                num_counter += 1
                scout_ptr += 1

            # print("MIDDLE")
            # print("build_ptr ", build_ptr)
            # print("mem_num ", mem_num)
            # print("num_counter ", num_counter)
            # print("scout_ptr ", scout_ptr)
            # print("nums ", nums)
            # print("------------------")

            for _ in range(min(2, num_counter)):
                nums[build_ptr] = mem_num
                build_ptr += 1
                num_counter -= 1

            mem_num = nums[min(scout_ptr, len(nums) - 1)]
            num_counter = 0

            # print("END")
            # print("build_ptr ", build_ptr)
            # print("mem_num ", mem_num)
            # print("num_counter ", num_counter)
            # print("scout_ptr ", scout_ptr)
            # print("nums ", nums)
            # print("====================")

        return build_ptr


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
# output: 5
# nums becomes [1,1,2,2,3, _]
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
# output: 7
# nums becomes [0,0,1,1,2,3,3,_,_]
