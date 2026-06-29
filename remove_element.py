from typing import List


def removeElement(nums: List[int], val: int) -> int:
    val_counter = 0  # counter for the end result
    pt = 0  # stepper for where we are at
    max_pos = len(nums) - 1  # flag for the end of the nums list
    container = []

    # edge cases
    # 1. what happens when pt reaches the max_pos - 1? it becomes max_pos at last line
    # it goes back to the loop, do the compmarison, add 1 more at the end and gets rejected by the loop condition
    while pt <= max_pos:
        print(f"pointer at {pt}")
        print(f"current of val count {val_counter}")
        print(f"status of nums {' '.join([str(e) for e in nums])}")
        if nums[pt] == val:
            nums[pt] = -1  # because the nums element can't smaller than 1
            val_counter += 1
        else:
            container.append(nums[pt])

        pt += 1

    print("container is ", container)
    for i, e in enumerate(container):
        nums[i] = e

    print(f"final val count {val_counter}")
    print("final list ", nums)

    return val_counter


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
