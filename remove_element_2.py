from typing import List


def removeElement(nums: List[int], val: int) -> int:
    scout_ptr = 0
    build_ptr = 0

    while scout_ptr < len(nums):
        if nums[scout_ptr] != val:
            nums[build_ptr] = nums[scout_ptr]

            build_ptr += 1

        scout_ptr += 1

    return build_ptr


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
