from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return self.trap_twoPass(height)

    def trap_bruteForce(self, height: List[int]) -> int:
        total = 0
        max_left = height[0]
        for i in range(1, len(height) - 1):
            max_left = max(max_left, height[i - 1])
            max_right = max(height[i + 1 : len(height)])
            can_hold = max(min(max_left, max_right) - height[i], 0)
            print(
                f"i: {i}, max_left: {max_left}, max_right: {max_right}, can_hold: {can_hold}"
            )
            total += can_hold

        return total

    def trap_twoPass(self, height: List[int]) -> int:
        total = 0
        max_left = height[0]
        max_right = height[len(height) - 1]
        max_left_list = [height[0]] * len(height)
        max_right_list = [height[len(height) - 1]] * len(height)
        for i, j in zip(range(1, len(height) - 1), range(len(height) - 2, -1, -1)):
            max_left = max(max_left, height[i - 1])
            max_left_list[i] = max_left
            max_right = max(max_right, height[j + 1])
            max_right_list[j] = max_right

        can_hold = [min(l, r) for l, r in zip(max_left_list, max_right_list)]
        total = sum(can_hold)

        return total


solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), " ", 6)

print("------------------------")
solution = Solution()
print(solution.trap([4, 2, 0, 3, 2, 5]), " ", 9)
