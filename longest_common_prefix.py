from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.longestCommonPrefix_inplace(strs)

    def longestCommonPrefix_createSubStr(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(0, min([len(e) for e in strs])):
            prefix += strs[0][i]
            for word in strs:
                print(
                    "word till i is | ",
                    word[0 : i + 1],
                    "| prefix plus this char is | ",
                    prefix,
                    "|",
                )

                if word[0 : i + 1] != prefix:
                    return prefix[:-1]

        return prefix

    def longestCommonPrefix_inplace(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            for other_word in strs[1:]:
                print(
                    "word till i is | ",
                    strs[0][0 : i + 1],
                    "| other_word till i is | ",
                    other_word[0 : i + 1],
                    "|",
                )
                if len(other_word) < i + 1 or strs[0][i] != other_word[i]:
                    return strs[0][:i]
            i += 1

        return strs[0]


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print("---------------------------")


solution = Solution()
print(solution.longestCommonPrefix(["ab", "a"]))
