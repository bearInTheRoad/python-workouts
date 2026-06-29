from typing import List


def removeDuplicates(nums: List[int]) -> int:
    mem_num = nums[0]
    scout_ptr = 1
    build_ptr = 1

    while scout_ptr < len(nums):
        if mem_num != nums[scout_ptr]:
            nums[build_ptr] = nums[scout_ptr]
            mem_num = nums[scout_ptr]
            build_ptr += 1
        print("mem_num ", mem_num)
        print("scout_ptr", scout_ptr)
        print("build_ptr", build_ptr)
        print("nums ", nums)
        print("---------------------")
        scout_ptr += 1

    return build_ptr


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
