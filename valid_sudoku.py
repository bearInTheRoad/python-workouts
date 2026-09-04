from typing import List
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            total = Counter(row)
            del total["."]
            if len(total) > 0 and total.most_common(1)[0][1] > 1:
                return False

        for column in range(9):
            total = Counter([board[row][column] for row in range(9)])
            del total["."]
            if len(total) > 0 and total.most_common(1)[0][1] > 1:
                print(total)
                return False

        subbox = [[] for _ in range(9)]
        for row in range(9):
            for column in range(9):
                group = (column // 3) * 3 + (row // 3)
                subbox[group].append(board[row][column])

        for group in subbox:
            total = Counter(group)
            del total["."]
            if len(total) > 0 and total.most_common(1)[0][1] > 1:
                print(total)
                return False

        return True


solution = Solution()
print(
    solution.isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

print(
    solution.isValidSudoku(
        [
            ["7", ".", ".", ".", "4", ".", ".", ".", "."],
            [".", ".", ".", "8", "6", "5", ".", ".", "."],
            [".", "1", ".", "2", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "9", ".", ".", "."],
            [".", ".", ".", ".", "5", ".", "5", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
)
