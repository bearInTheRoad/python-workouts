class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.strStr_naive(haystack, needle)

    def strStr_naive(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1
        for i in range(len(haystack) - len(needle) + 1):
            match_num = 0
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                match_num += 1
            if match_num == len(needle):
                return i
        return -1

    def strStr_kmp(self, haystack: str, needle: str) -> int:
        return -1


solution = Solution()
print(solution.strStr("hello", "ll"), 2)
print("-----------------------")

solution = Solution()
print(solution.strStr("sadbutsad", "sad"), 0)
print("-----------------------")

solution = Solution()
print(solution.strStr("leetcode", "leeto"), -1)
print("-----------------------")

solution = Solution()
print(solution.strStr("aaa", "aaaa"), -1)
print("-----------------------")


solution = Solution()
print(solution.strStr("mississippi", "issipi"), -1)
print("-----------------------")

solution = Solution()
print(solution.strStr("abc", "c"), 2)

