class Solution:
    def romanToInt(self, s: str) -> int:
        return self.romanToInt_reversed(s)

    def romanToInt_simulation(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        subtract = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        i = 0
        ans = 0
        end_flag = "mapping"
        while i < len(s) - 1:
            if mapping[s[i]] < mapping[s[i + 1]]:
                ans += subtract[s[i : i + 2]]
                i += 2
                end_flag = "subtract"
            else:
                ans += mapping[s[i]]
                i += 1
                end_flag = "mapping"

        if end_flag == "mapping" or (end_flag == "subtract" and s[-3:-1] in (subtract)):
            ans += mapping[s[-1]]

        return ans

    def romanToInt_elegant(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        i = 0
        ans = 0

        while i < len(s) - 1:
            if mapping[s[i]] < mapping[s[i + 1]]:
                ans -= mapping[s[i]]
            else:
                ans += mapping[s[i]]
            i += 1

        ans += mapping[s[-1]]

        return ans

    def romanToInt_reversed(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        i = len(s) - 1
        ans = 0

        while i > 0:
            if mapping[s[i]] <= mapping[s[i - 1]]:
                ans += mapping[s[i - 1]]
            else:
                ans -= mapping[s[i - 1]]
            i -= 1

        ans += mapping[s[-1]]

        return ans


solution = Solution()
print(solution.romanToInt("III"), 3)

print("------------------------")
solution = Solution()
print(solution.romanToInt("LVIII"), 58)

print("------------------------")
solution = Solution()
print(solution.romanToInt("MCMXCIV"), 1994)

print("------------------------")
solution = Solution()
print(solution.romanToInt("XCV"), 95)
