import math


class Solution:
    def intToRoman(self, num: int) -> str:
        return self.intToRoman_firstThough(num)

    def intToRoman_firstThough(self, num: int) -> str:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        subtract = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        thousands = [("M", 1000), ("M", 1000), ("M", 1000)]
        hundreds = [
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("C", 100),
            ("C", 100),
        ]
        tens = [("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("X", 10), ("X", 10)]
        ones = [("IX", 9), ("V", 5), ("IV", 4), ("I", 1), ("I", 1), ("I", 1)]

        num_thousands = math.floor(num / 1000) * 1000
        num_hundres = math.floor((num - num_thousands) / 100) * 100
        num_tens = math.floor((num - num_thousands - num_hundres) / 10) * 10
        num_ones = num - num_thousands - num_hundres - num_tens

        end_roman = ""
        for k, v in thousands:
            print(num_thousands)
            if num_thousands - v >= 0:
                num_thousands -= v
                end_roman += k
                print("In thousands")
                print(end_roman)
                print("----------")

        for k, v in hundreds:
            print(num_hundres)
            if num_hundres - v >= 0:
                num_hundres -= v
                end_roman += k
                print("In hundreds")
                print(end_roman)
                print("----------")

        for k, v in tens:
            print(num_tens)
            if num_tens - v >= 0:
                num_tens -= v
                end_roman += k
                print("In tens")
                print(end_roman)
                print("----------")

        for k, v in ones:
            print(num_ones)
            if num_ones - v >= 0:
                num_ones -= v
                end_roman += k
                print("In ones")
                print(end_roman)
                print("----------")

        return end_roman

    def intToRoman_secondSimpler(self, num):
        num_list = [
            ("M", 1000),
            ("M", 1000),
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("C", 100),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("X", 10),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
            ("I", 1),
            ("I", 1),
        ]

        end_roman = ""
        for k, v in num_list:
            if num - v >= 0:
                num -= v
                end_roman += k

        return end_roman


solution = Solution()
print(solution.intToRoman(3749))
print("-------------------------")

solution = Solution()
print(solution.intToRoman(58))
print("-------------------------")

solution = Solution()
print(solution.intToRoman(1994))
print("-------------------------")
