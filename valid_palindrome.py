import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = re.sub(r"[^a-zA-Z0-9]", "", s)
        left_ptr = 0
        right_ptr = len(normalized_s) - 1
        while left_ptr < right_ptr:
            if normalized_s[left_ptr].lower() != normalized_s[right_ptr].lower():
                return False
            left_ptr += 1
            right_ptr -= 1
        return True

    def isPalindrome_flipped(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list

    def isPalindrome_twoPointers_onthefly(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))
s = "OP"
print(solution.isPalindrome(s))
