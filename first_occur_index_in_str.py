class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.strStr_kmp(haystack, needle)

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
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # PREPROCESSING
        # longest border array
        longest_border = [0] * m
        # Length of Longest Border for prefix before it.
        prev = 0
        # Iterating from index-1. longest_border[0] will always be 0
        i = 1

        while i < m:
            if needle[i] == needle[prev]:
                # Length of Longest Border Increased
                prev += 1
                longest_border[i] = prev
                i += 1
            else:
                # Only empty border exist
                if prev == 0:
                    longest_border[i] = 0
                    i += 1
                # Try finding longest border for this i with reduced prev
                else:
                    prev = longest_border[prev - 1]

        # SEARCHING
        # Pointer for haystack
        haystack_pointer = 0
        # Pointer for needle.
        # Also indicates number of characters matched in current window.
        needle_pointer = 0

        while haystack_pointer < n:
            if haystack[haystack_pointer] == needle[needle_pointer]:
                # Matched Increment Both
                needle_pointer += 1
                haystack_pointer += 1
                # All characters matched
                if needle_pointer == m:
                    # m characters behind last matching will be window start
                    return haystack_pointer - m
            else:
                if needle_pointer == 0:
                    # Zero Matched
                    haystack_pointer += 1
                else:
                    # Optimally shift left needle_pointer.
                    # Don't change haystack_pointer
                    needle_pointer = longest_border[needle_pointer - 1]

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

