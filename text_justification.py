from typing import List
import math


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

        line_len_list = []
        for e in output:
            line_len = 0
            for s in e:
                line_len += len(s)
            line_len_list.append(line_len)
        print(line_len_list)

        new_output = []
        for (line_index, group), group_len in zip(enumerate(output), line_len_list):
            ttl_space_count = maxWidth - group_len
            print("extra space is ", ttl_space_count)

            new_string = ""
            # if the group is only with 1 word, all padded to the left
            if len(group) == 1:
                new_string += group[0] + " " * ttl_space_count

            elif line_index == len(output) - 1 and len(group) != 1:
                new_string += " ".join(group)
                new_string += " " * (maxWidth - len(new_string))

            else:
                while ttl_space_count > 0:
                    consumed_space = 0
                    for index in range(len(group) - 1):
                        group[index] += " "
                        consumed_space += 1
                        if ttl_space_count - consumed_space <= 0:
                            break
                    ttl_space_count -= consumed_space

                new_string = "".join(group)

            print(new_string)

            new_output.append(new_string)

        return new_output


solution = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
output = solution.fullJustify(words, 16)
print(output)
print([len(element) for element in output])
print(["This    is    an", "example  of text", "justification.  "])
print("--------------------------")

words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
output = solution.fullJustify(words, 16)
print(output)
print([len(element) for element in output])
print(["What   must   be", "acknowledgment  ", "shall be        "])


words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
maxWidth = 20
output = solution.fullJustify(words, 20)
print(output)
print([len(element) for element in output])
print(
    [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
)
