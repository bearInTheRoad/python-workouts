from typing import List


class Solution:
    """
    The complicated part is you need to consider the i + 1 may change again
    after you deterine what should be the value on i


    if all elements only go uphill, then there is no problem
    the issue emreges when it goes up and down, then at the subsequent elements
    after the peak, you will need to consider the previous element
    """

    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)

        for i in range(len(ratings)):
            if i == 0:
                if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                    candy[i] += 1
            elif i == len(ratings) - 1:
                if ratings[i] > ratings[i - 1] and candy[i] <= candy[i - 1]:
                    candy[i] += 1
            else:
                print("index is ", i, " candy is ", candy, " ratings is ", ratings)
                if ratings[i] > ratings[i - 1]:
                    candy[i] = candy[i - 1] + 1
                elif ratings[i] < ratings[i - 1] and candy[i - 1] == 1:
                    candy[i] = candy[i - 1]
                    candy[i - 1] += 1

        print(ratings)
        print(candy)
        return sum(candy)


solution = Solution()
ratings = [1, 2, 87, 87, 87, 2, 1]
print(solution.candy(ratings), " 13")

print("----------------------------")
solution = Solution()
ratings = [29, 51, 87, 87, 72, 12]
print(solution.candy(ratings), " 12")
