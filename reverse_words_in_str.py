class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return self.convert_simulation(s, numRows)

    def convert_simulation(self, s: str, numRows: int) -> str:
        output = []
        gap = numRows + numRows - 2
        if numRows == 1:
            return s
        for row in range(numRows):
            # first row, no middle column concerns
            if row == 0:
                i = 0
                while i <= len(s) - 1:
                    output.append(s[i])
                    # top and botton row has no mid column
                    i += gap
            # last row, no middle column concerns
            elif row == numRows - 1:
                j = numRows - 1
                while j <= len(s) - 1:
                    output.append(s[j])
                    j += gap
            # middle rows, we start to consider mid column
            else:
                k = row
                while k <= len(s) - 1:
                    col_start = k - row
                    next_col_start = col_start + gap
                    output.append(s[k])
                    # now let's add in middle column, the index of which is
                    # the result of column start sum - k

                    # the if is to protect the case where next middle column is empty
                    if col_start + next_col_start - k <= len(s) - 1:
                        output.append(s[col_start + next_col_start - k])
                    k += gap
        return "".join(output)


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
print("---------------------")

solution = Solution()
print(solution.convert("PAYPALISHIRING", 4), "PAHNAPLSIIGYIR")
print("---------------------")
solution = Solution()

print(solution.convert("A", 3), "A")
print("---------------------")
