from typing import List
from collections import deque, defaultdict


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.numIslands_dfs(grid)

    def belongIslands(self, grid, row, column, islands, island_counts):

        if tuple([row, column]) in islands:
            return False

        if tuple([row + 1, column]) in islands:
            islands[tuple([row, column])] = islands[tuple([row + 1, column])]
            return False

        if tuple([row - 1, column]) in islands:
            islands[tuple([row, column])] = islands[tuple([row - 1, column])]
            return False

        if tuple([row, column + 1]) in islands:
            islands[tuple([row, column])] = islands[tuple([row, column + 1])]
            return False

        if tuple([row, column - 1]) in islands:
            islands[tuple([row, column])] = islands[tuple([row, column - 1])]
            return False

        islands[tuple([row, column])] = island_counts + 1

        print(islands)
        return True

    def numIslands_naive(self, grid: List[List[str]]) -> int:
        rows_count = len(grid)
        columns_count = len(grid[0])
        island_counts = 0
        islands = {}

        for row in range(rows_count):
            for column in range(columns_count):
                if grid[row][column] == "1" and self.belongIslands(
                    grid, row, column, islands, island_counts
                ):
                    island_counts += 1

        return island_counts

    def numIslands_bfs(self, grid: List[List[str]]) -> int:

        column_count = len(grid[0])
        row_count = len(grid)
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        # print(visited)
        islands_count = 0
        queue = deque()

        for row in range(row_count):
            for column in range(column_count):
                if visited[row][column]:
                    continue
                if grid[row][column] == "1":
                    visited[row][column] = True
                    queue.append((row, column))

                if queue:
                    islands_count += 1
                while queue:
                    # print(queue)
                    # print("before started ", visited)
                    x, y = queue.popleft()
                    # print(x, y)
                    if (
                        y < column_count - 1
                        and grid[x][y + 1] == "1"
                        and (not visited[x][y + 1])
                    ):
                        visited[x][y + 1] = True
                        queue.append((x, y + 1))
                    if y > 0 and grid[x][y - 1] == "1" and (not visited[x][y - 1]):
                        visited[x][y - 1] = True
                        queue.append((x, y - 1))
                    if (
                        x < row_count - 1
                        and grid[x + 1][y] == "1"
                        and (not visited[x + 1][y])
                    ):
                        visited[x + 1][y] = True
                        queue.append((x + 1, y))
                    if x > 0 and grid[x - 1][y] == "1" and (not visited[x - 1][y]):
                        visited[x - 1][y] = True
                        queue.append((x - 1, y))
                # print("after ", visited)

        return islands_count

    def numIslands_dfs(self, grid):
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or c >= len(grid[0]) or r >= len(grid) or grid[r][c] == "0":
            return

        grid[r][c] = "0"

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)


solution = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(solution.numIslands(grid), "1")

grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
print(solution.numIslands(grid), "1")

grid = [["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]]
print(solution.numIslands(grid), "4")
