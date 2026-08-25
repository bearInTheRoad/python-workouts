from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]):
        return self.findSubstring__slideWindow_shrink(s, words)

    # LT test cases TLE on the last one
    def findSubstring_firstBruteForce(self, s: str, words: List[str]) -> List[int]:

        index_list = []
        index_mapping = {}
        freq_list = {}
        word_len = len(words[0])
        for word in words:
            if freq_list.get(word, 0) == 0:
                freq_list[word] = 1
            else:
                freq_list[word] += 1

        i = 0
        while i < len(s):
            # print(s[i : i + word_len])
            if s[i : i + word_len] in words:
                index_mapping[i] = s[i : i + word_len]
                index_list.append(i)
            i += 1

        # print(index_list)
        # print(freq_list)
        # print(index_mapping)
        result = []
        for idx in sorted(index_list):
            this_word = index_mapping[idx]
            record_list = {this_word: 1}
            left = idx
            # print("------------")
            # print(left, this_word, record_list)
            while left < len(s):
                new_word = index_mapping.get(left + len(this_word))
                # print(new_word)
                current_freq = record_list.get(new_word, 0)
                if (not new_word) or (current_freq >= freq_list[new_word]):
                    break
                else:
                    record_list[new_word] = record_list.get(new_word, 0) + 1
                    left = left + len(this_word)
                    this_word = new_word

                # print(left, this_word, record_list)

            # print(freq_list, record_list)
            if freq_list == record_list:
                result.append(idx)

        return result

    # Passed LT test cases
    def findSubstring__betterBruteForce(self, s: str, words: List[str]) -> List[int]:

        freq_list = {}
        word_len = len(words[0])
        freq_list = Counter(words)

        # print(index_list)
        # print(freq_list)
        # print(index_mapping)
        result = []
        record_list = Counter()
        for offset in range(word_len):
            ptr = offset
            # print("===================")
            # print("offset is ", offset)

            while ptr < len(s):
                word = s[ptr : ptr + word_len]

                # print(word)
                if word in freq_list:
                    target = s[ptr : ptr + word_len * len(words)]
                    chunks = [
                        target[i : i + word_len]
                        for i in range(0, len(target), word_len)
                    ]
                    # print(chunks)
                    record_list = Counter(chunks)

                    if record_list == freq_list:
                        result.append(ptr)

                ptr += word_len

        return result

    def findSubstring__slideWindow_fixed(self, s: str, words: List[str]) -> List[int]:

        freq_list = {}
        word_len = len(words[0])
        freq_list = Counter(words)

        result = []
        for offset in range(word_len):
            ptr = offset
            # print("===================")
            # print("offset is ", offset)

            target = s[ptr : ptr + word_len * len(words)]
            chunks = [target[i : i + word_len] for i in range(0, len(target), word_len)]
            # print(chunks)
            record_list = Counter(chunks)
            while ptr < len(s):
                # print(record_list)
                if record_list == freq_list:
                    result.append(ptr)
                record_list[s[ptr : ptr + word_len]] -= 1
                ptr += word_len
                record_list[
                    s[
                        ptr + word_len * len(words) - word_len : ptr
                        + word_len * len(words)
                    ]
                ] += 1

        return result

    def findSubstring__slideWindow_shrink(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        freq_list = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            record = Counter()
            valid_count = 0  # how many words in window are "used" validly

            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len

                if word in freq_list:
                    record[word] += 1
                    valid_count += 1

                    # shrink while we have too many of this word
                    while record[word] > freq_list[word]:
                        left_word = s[left : left + word_len]
                        record[left_word] -= 1
                        valid_count -= 1
                        left += word_len

                    # window has exactly all words
                    if valid_count == total_words:
                        result.append(left)
                else:
                    # invalid word: reset window entirely
                    record.clear()
                    valid_count = 0
                    left = right

        return result


solution = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(solution.findSubstring(s, words), [0, 9])

s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(solution.findSubstring(s, words), [])

s = "barfoofoobarthefoobarman"
words = ["foo", "bar", "the"]
print(solution.findSubstring(s, words), [6, 9, 12])


s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
print(solution.findSubstring(s, words), [8])

s = "ababababab"
words = ["ababa", "babab"]
print(solution.findSubstring(s, words), [0])

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo", "barr", "wing", "ding", "wing"]
print(solution.findSubstring(s, words), [13])

s = "aaaaaaaaaaaaaa"
words = ["aa", "aa"]
print(solution.findSubstring(s, words), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
