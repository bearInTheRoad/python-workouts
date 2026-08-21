class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.lengthOfLongestSubstring_optimizedSlideWindow(s)

    def lengthOfLongestSubstring_bruteforce(self, s: str) -> int:

        if len(s) == 0:
            return 0

        left = 0

        max_length = 1
        for right in range(1, len(s)):
            while left < right:
                if s[left] in s[left + 1 : right + 1]:
                    left += 1
                elif s[right] in s[left:right]:
                    left += 1
                else:
                    max_length = max(max_length, right - left + 1)
                    break

            print(s[left : right + 1], max_length)

        return max_length

    def lengthOfLongestSubstring_slidingWindow(self, s: str) -> int:

        if len(s) == 0:
            return 0

        left = 0

        max_length = 1

        seen = set(s[0])
        for right in range(1, len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            max_length = max(max_length, right - left + 1)
            seen.add(s[right])

        return max_length

    def lengthOfLongestSubstring_optimizedSlideWindow(self, s: str) -> int:

        mapping = {}

        left = 0

        max_length = 0
        for right in range(0, len(s)):
            if s[right] in mapping and mapping[s[right]] >= left:
                left = mapping[s[right]]
                left += 1

            max_length = max(max_length, right - left + 1)
            mapping[s[right]] = right

            print(left, right)
            print(mapping)
            print(max_length)

        return max_length


solution = Solution()
# s = "abcabcbb"
# print(solution.lengthOfLongestSubstring(s), 3)
#
# s = "bbbb"
# print(solution.lengthOfLongestSubstring(s), 1)
#
#
# s = "pwwkew"
# print(solution.lengthOfLongestSubstring(s), 3)
#
# s = "mq"
# print(solution.lengthOfLongestSubstring(s), 2)
#
# s = "<Dx"
# print(solution.lengthOfLongestSubstring(s), 3)
#
# s = "7stsUB"
# print(solution.lengthOfLongestSubstring(s), 4)

s = "ccbbcc"
print(solution.lengthOfLongestSubstring(s), 2)
