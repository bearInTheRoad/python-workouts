import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return self.convert_simulation(s, numRows)

    def convert_simulation(self, s: str, numRows: int) -> str:
        output = ""
        if numRows == 1:
            return s
        for row in range(numRows):
            # first row, no middle column concerns
            if row == 0 or row == numRows - 1:
                i = 0 if row == 0 else numRows - 1
                while i <= len(s) - 1:
                    output += s[i]
                    # top and botton row has no mid column
                    i += numRows + (numRows - 2)
            # middle rows, we start to consider mid column
            else:
                k = row
                while k <= len(s) - 1:
                    col_start = math.floor(k / (numRows + numRows - 2)) * (
                        numRows + numRows - 2
                    )
                    next_col_start = col_start + (numRows + numRows - 2)
                    output += s[k]
                    # now let's add in middle column, the index of which is
                    # the result of column start sum - k

                    # the if is to protect the case where next middle column is empty
                    if col_start + next_col_start - k <= len(s) - 1:
                        output += s[col_start + next_col_start - k]
                    k += numRows + (numRows - 2)
        return output

    def convert_simulation_aiOptimzied(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s) - 1
        gap = numRows + numRows - 2
        output = []

        for row in range(numRows):
            # first and last row: no middle column, single hit per cycle
            if row == 0 or row == numRows - 1:
                i = 0 if row == 0 else numRows - 1
                while i <= n:
                    output.append(s[i])
                    i += gap
            # middle rows: vertical hit at k, diagonal hit at k + gap - 2*row
            else:
                k = row
                mid_offset = gap - 2 * row
                while k <= n:
                    output.append(s[k])
                    mid = k + mid_offset
                    if mid <= n:
                        output.append(s[mid])
                    k += gap

        return "".join(output)

    def convert_simulation_leetcode(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = []
        n = len(s)
        chars_in_section = 2 * (numRows - 1)

        for curr_row in range(numRows):
            index = curr_row
            while index < n:
                answer.append(s[index])

                # If curr_row is not the first or last row,
                # then we have to add one more character of current section.
                if curr_row != 0 and curr_row != numRows - 1:
                    chars_in_between = chars_in_section - 2 * curr_row
                    second_index = index + chars_in_between

                    if second_index < n:
                        answer.append(s[second_index])
                # Jump to same row's first character of next section.
                index += chars_in_section

        return "".join(answer)


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
print("---------------------")

solution = Solution()
print(solution.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
print("---------------------")
solution = Solution()

print(solution.convert("A", 3), "A")
print("---------------------")

