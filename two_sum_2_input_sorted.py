from typing import List


class Solution:
    def twoSum_hashmap(self, numbers: List[int], target: int) -> List[int]:

        hash_map = {}
        for i, e in enumerate(numbers):
            hash_map[e] = i

        for i, e in enumerate(numbers):
            if hash_map.get(target - e):
                return [i + 1, hash_map[target - e] + 1]

        return [0, 0]

    def twoSum_twoPointer(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i != j:
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
            print(i, j)

        return [i + 1, j + 1]


solution = Solution()
print(solution.twoSum_twoPointer([2, 7, 11, 15], 9))
