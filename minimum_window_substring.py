from collections import Counter


def compare_counter(freq_list, record_list):

    for key in freq_list:
        if freq_list[key] > record_list[key]:
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        if len(t) == len(s) and t == s:
            return t

        if len(t) == 0 or len(s) == 0:
            return ""

        freq_list = Counter(t)

        left, right = 0, 0

        min_window = 10**5 + 1
        min_index = (0, 0)

        record_list = Counter()
        print(freq_list)

        while right < len(s):
            print("-----right ptr move-------")
            print(left, right, s[left : right + 1], min_index)

            if s[right] in freq_list:
                record_list[s[right]] += 1

            while (
                left <= right
                and left < len(s)
                and (
                    (s[left] not in freq_list)
                    or (record_list[s[left]] > freq_list[s[left]])
                )
            ):
                if s[left] in freq_list:
                    record_list[s[left]] -= 1
                left += 1

            print(freq_list)
            print(record_list)
            print(compare_counter(freq_list, record_list))
            if min_window > right - left + 1 and compare_counter(
                freq_list, record_list
            ):
                min_window = right - left + 1
                min_index = (left, right)
            right += 1

        if min_window > right - left + 1 and min_window != 10**5 + 1:
            min_window = right - left + 1
            min_index = (left, right)

        return s[min_index[0] : min_index[1] + 1] if min_window != 10**5 + 1 else ""


solution = Solution()
# print(solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")

# print(solution.minWindow("a", "b"), "")
#
# print(solution.minWindow("ab", "a"), "a")
#
# print(solution.minWindow("ab", "A"), "")
#
# print(solution.minWindow("abc", "cba"), "abc")
#
# print(solution.minWindow("cabwefgewcwaefgcf", "cae"), "cwae")
#
# print(solution.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"), "abbbbbcdd")

print(solution.minWindow("babb", "baba"), "")
