from typing import List


class Solution:
    def next_direction(
        self, current_pos, last_direction, row_count, column_count, visited
    ):
        row, column = current_pos

        print(visited, current_pos)
        if last_direction == "right":
            return (
                "down"
                if column + 1 >= column_count or column + 1 >= visited["right"]
                else "right"
            )

        if last_direction == "left":
            return "up" if column - 1 < 0 or column - 1 <= visited["left"] else "left"

        if last_direction == "up":
            return "right" if row - 1 < 0 or row - 1 <= visited["up"] else "up"

        if last_direction == "down":
            return (
                "left" if row + 1 >= row_count or row + 1 >= visited["down"] else "down"
            )

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_count = len(matrix)
        column_count = len(matrix[0])
        visited = {
            "left": -1,
            "right": row_count,
            "up": -1,
            "down": column_count,
        }  # left, right, up, down, max visited
        result = []

        ptr = (0, 0)
        last_direction = "right"

        while len(result) < row_count * column_count:
            result.append(matrix[ptr[0]][ptr[1]])
            next_direction = self.next_direction(
                ptr, last_direction, row_count, column_count, visited
            )

            if last_direction != next_direction:
                if last_direction == "right":
                    visited["up"] = ptr[0]
                if last_direction == "left":
                    visited["down"] = ptr[0]
                if last_direction == "up":
                    visited["left"] = ptr[1]
                if last_direction == "down":
                    visited["right"] = ptr[1]
                last_direction = next_direction

            if next_direction == "right":
                ptr = (ptr[0], ptr[1] + 1)
            elif next_direction == "left":
                ptr = (ptr[0], ptr[1] - 1)
            elif next_direction == "up":
                ptr = (ptr[0] - 1, ptr[1])
            else:
                ptr = (ptr[0] + 1, ptr[1])

        return result


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert solution.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5], (
    solution.spiralOrder(matrix)
)
