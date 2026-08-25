from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        if len(t) == len(s) and t == s:
            return t

        if len(t) == 0 or len(s) == 0:
            return ""

        freq_list = Counter(t)

        valid_count = 0

        left, right = 0, 0

        min_window = 10**5 + 1
        min_index = (0, 0)

        record_list = Counter()

        while right < len(s):
            print(left, right, valid_count, s[left : right + 1])

            while (
                (s[right] in freq_list and record_list[s[right]] >= freq_list[s[right]])
                or (
                    s[left] not in freq_list
                    and record_list[s[left]] > freq_list[s[left]]
                )
            ) and left <= right:
                if s[left] in freq_list:
                    valid_count -= 1
                    record_list[s[left]] -= 1
                left += 1

            if s[right] in freq_list and record_list[s[right]] < freq_list[s[right]]:
                record_list[s[right]] += 1
                valid_count += 1

            if valid_count == len(t) and min_window > left - right:
                min_window = right - left + 1
                min_index = (left, right)

            right += 1

        while right >= len(s):
            right -= 1
        print(left, right, valid_count, min_window, s[left : right + 1])
        while (
            valid_count < right - left + 1
            and s[left] not in freq_list
            and left <= right
        ):
            left += 1

        while left > right:
            left -= 1
        print(left, right, valid_count, min_window, s[left : right + 1])
        while (
            valid_count < right - left + 1
            and s[right] not in freq_list
            and left <= right
        ):
            right -= 1
        if min_window > right - left + 1:
            min_window = right - left + 1
            min_index = (left, right)

        return s[min_index[0] : min_index[1] + 1]


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")

print(solution.minWindow("a", "b"), "")

print(solution.minWindow("ab", "a"), "")

print(solution.minWindow("ab", "A"), "")

print(solution.minWindow("abc", "cba"), "abc")

print(solution.minWindow("cabwefgewcwaefgcf", "cae"), "cwae")
