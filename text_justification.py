from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = [[]]
        i = 0  # ptr for words
        j = 0  # ptr for output
        line_len = 0
        while i < len(words):
            if line_len + len(words[i]) <= maxWidth:
                output[j].append(words[i])
                line_len += len(words[i]) + 1
                i += 1
            else:
                output.append([])
                line_len = 0
                j += 1
            print(output)

        output = [f"{''.join(group):<{maxWidth}}" for group in output]

        return output


solution = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
print(solution.fullJustify(words, 16))
