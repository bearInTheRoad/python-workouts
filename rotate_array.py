from typing import List


class solution:
    def rotate(self, nums: list[int], k: int) -> none:
        """
        do not return anything, modify nums in-place instead.
        """
        # # linear write -- passed, but inefficient
        # for i in range(k):
        #     nums.insert(0, nums.pop(-1))

        # won't work without [:] - list is an assignment, slicing and adding is creating new space
        # but if you go with slicing, it can work. the new array will be copeid into the existing object
        k %= len(nums)
        nums[:] = nums[len(nums) - k : len(nums)] + nums[0 : len(nums) - k]

        # smarter linear write -- failed
        # nums[0: 0] = nums[len(nums) - k: len(nums)]
        # del nums[len(nums) - k: len(nums)]

        ##### reverse - most optimal way, but boring
        # n = len(nums)
        # # a common sense is if you rotate just by n or the times of n
        # # the array is already in the right order
        # # see if k is smaller than n
        # # if k > n: , return the reminder
        # # if k < 0: return the k
        # k %= n
        # print('k%=n, ', k)
        #
        # def reverse(l, r):
        #     # in cases where there is odd number of elements
        #     # the one in the middle won't be reversed because
        #     while l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r -= 1
        #
        # print('-----------------')
        # # do a complete reverse on all elements
        # reverse(0, n-1)
        #
        # print('after first swap ', nums)
        # # do a reverse on the first k elements
        # reverse(0, k-1)
        # print('after second swap ', nums)
        # reverse(k, n-1)
        # print('after third swap ', nums)
        # print('-----------------')


solution = solution()
list1 = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(list1, 3)
print(list1)
list2 = [-1, -100, 3, 99]
solution.rotate(list2, 2)
print(list2)
list3 = [1, 2, 3]
solution.rotate(list3, 5)
list4 = [1, 2, 3]
solution.rotate(list4, 3)
