class Solution:
    def isSubsequence_TwoPointers(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while j <= len(t) - 1 and i <= len(s) - 1:
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        return False

    def isSubsequence_Hashmap(self, s: str, t: str) -> bool:

        map = {}
        for i, e in enumerate(t):
            if map.get(e):
                map[e].append(i)
            else:
                map[e] = [i]

        pointer = -1
        for e in s:
            if e not in map.keys():
                return False
            else:
                if pointer >= max(map[e]):
                    return False
                else:
                    print(pointer)
                    pointer = min([i for i in map[e] if i > pointer])

        return True


solution = Solution()

s = "abc"
t = "ahbgdc"
print(solution.isSubsequence_TwoPointers(s, t))
print(solution.isSubsequence_Hashmap(s, t))

print("==========================")
s = "axc"
t = "ahbgdc"
print(solution.isSubsequence_TwoPointers(s, t))
print(solution.isSubsequence_Hashmap(s, t))

print("==========================")
s = "ac"
t = "ahbgdc"
print(solution.isSubsequence_TwoPointers(s, t))
print(solution.isSubsequence_Hashmap(s, t))


print("==========================")
s = ""
t = ""
print(solution.isSubsequence_TwoPointers(s, t))
print(solution.isSubsequence_Hashmap(s, t))

print("==========================")
s = "aaaaaa"
t = "bbaaaa"
print(solution.isSubsequence_TwoPointers(s, t))
print(solution.isSubsequence_Hashmap(s, t))
