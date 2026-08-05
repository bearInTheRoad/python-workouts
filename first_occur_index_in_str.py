import math


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.strStr_rp(haystack, needle)

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

    def strStr_rp(self, haystack: str, needle: str) -> int:
        """
        This is not the standard implementation of radian karp.
        I'm not considering int overflow here, which can be dangerous for other languages
        Also I'm not using ord(c) - ord(a) pattern to make it consistent to base 26 math
        It's currently using polynomial as positional fingerprints
        """
        if len(haystack) < len(needle):
            return -1

        target_num = sum(
            [ord(e) * (26 ** (len(needle) - i)) for i, e in enumerate(needle)]
        )

        start = 0
        end = start + len(needle)
        current_num = sum(
            [
                ord(e) * (26 ** (len(needle) - i))
                for i, e in enumerate(haystack[start:end])
            ]
        )
        while end <= len(haystack):
            print(
                f"start {start} {haystack[start]}, end {end} {haystack[end - 1]}, current_num {current_num}, target_num {target_num}"
            )
            if current_num == target_num:
                flag = True
                for e1, e2 in zip(needle, haystack[start:end]):
                    print(e1, e2)
                    if e1 != e2:
                        flag = False
                        break
                if flag:
                    return start

            if end < len(haystack):
                current_num = (
                    current_num - ord(haystack[start]) * (26 ** len(needle))
                ) * 26
                current_num += ord(haystack[end]) * 26
            start += 1
            end += 1

        return -1


solution = Solution()
print(solution.strStr("hello", "ll"), 2)
print("-----------------------")

solution = Solution()
print(solution.strStr("hell", "ll"), 2)
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
