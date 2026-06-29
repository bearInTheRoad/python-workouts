from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for element in nums:
            print("element ", element)
            if i == 0 or i == 1 or nums[i - 2] != element:
                nums[i] = element
                i += 1
                print("i ", i)

        print(nums)
        return i


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
# output: 5
# nums becomes [1,1,2,2,3, _]
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
# output: 7
# nums becomes [0,0,1,1,2,3,3,_,_]
