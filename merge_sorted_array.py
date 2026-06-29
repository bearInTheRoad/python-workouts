from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    pt1 = m - 1  # pointer for nums1
    pt2 = n - 1  # pointer for nums2
    pt3 = len(nums1) - 1  # pointer for filling in the holes in nums1

    while pt1 >= 0 or pt2 >= 0:
        # if pt1 is exhausted, fill in with pt2 numbers
        if pt1 < 0:
            nums1[pt3] = nums2[pt2]
            pt2 -= 1
        # if pt2 is exhausted, fill in with pt1 numbers
        elif pt2 < 0:
            nums1[pt3] = nums1[pt1]
            pt1 -= 1
        # if pt2 points a number bigger than pt1 poined number
        elif nums1[pt1] < nums2[pt2]:
            nums1[pt3] = nums2[pt2]
            pt2 -= 1
        # if pt1 points a number bigger than pt2 pointed number
        elif nums1[pt1] >= nums2[pt2]:
            nums1[pt3] = nums1[pt1]
            pt1 -= 1

        pt3 -= 1
        print(f"pt1 {pt1}")
        print(f"pt2 {pt2}")
        print(f"pt3 {pt3}")
        print(nums1)


# case 1
# 2 from nums2
# compare with 1 from nums1, index 0, bigger
# compare with 2 from nums1, index 1, equal
# insert at index 1
# 5 from nums2
# compare with 3 from nums 1, index 3


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, 3, nums2, 3)
print(nums1)
