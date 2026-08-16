from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.maxArea_twoPointers(height)

    def maxArea_bruteforce(self, height: List[int]) -> int:

        maxArea = 0
        for i_left, left in enumerate(height):
            for i_right in range(i_left + 1, len(height)):
                right = height[i_right]
                area = min(left, right) * (i_right - i_left)
                print("left and right are ", left, right)
                print("i_left and i_right are ", i_left, i_right)
                print("area is ", area)
                if area > maxArea:
                    maxArea = area
                print("max area is ", maxArea)

        return maxArea

    def maxArea_twoPointers(self, height: List[int]) -> int:
        """
        Proof: https://leimao.github.io/blog/Proof-Container-With-Most-Water-Problem/
        """
        left = 0
        right = len(height) - 1
        current_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            current_area = max(area, current_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return current_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
print(solution.maxArea(height))
height = [1, 1]
print(solution.maxArea(height))
height = [1, 2, 3, 1000, 9]
print(solution.maxArea(height))
