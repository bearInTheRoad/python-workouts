# Implement the RandomizedSet class:
#
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
#
#
#
# Example 1:
#
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
#
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
#
#
# Constraints:
#
# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.


class RandomizedSet:
    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if self.dict.get(val, None) is not None:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if self.dict.get(val) is None:
            return False
        val_index = self.dict[val]
        last_value_in_list = self.list[-1]
        self.list[val_index], self.list[-1] = self.list[-1], self.list[val_index]
        self.dict[val], self.dict[last_value_in_list] = (
            self.dict[last_value_in_list],
            self.dict[val],
        )
        self.dict.pop(val)
        self.list.pop()

        return True

    def getRandom(self) -> int:
        from random import randint

        picked = randint(0, max(len(self.list) - 1, 0))
        return self.list[picked]


class RandomizedSetPythonSet:
    def __init__(self):
        self.rs = set()
        self.len = 0

    def insert(self, val: int) -> bool:
        self.rs.add(val)
        if self.len == len(self.rs):
            return False
        self.len = len(self.rs)
        return True

    def remove(self, val: int) -> bool:
        try:
            self.rs.remove(val)
            self.len -= 1
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        from random import randint

        picked = randint(0, self.len - 1)
        return list(self.rs)[picked]


# random = RandomizedSet()
# print(random.insert(1), True)
# print(random.remove(2), False)
# print(random.insert(2), True)
# print(random.getRandom(), "1 or 2")
# print(random.remove(1), True)
# print(random.insert(2), False)
# print(random.getRandom(), 2)

print("------------------------------")

# [[],[0],[0],[0],[],[0],[0]]
# random = RandomizedSet()
# print(random.remove(0), True)
# print(random.remove(0), False)
# print(random.insert(0), True)
# print(random.getRandom(), "1 or 2")
# print(random.remove(0), True)
# print(random.insert(0), False)

# [[],[0],[1],[0],[2],[1],[]]
random = RandomizedSet()
print(random.insert(0), True)
print(random.insert(1), True)
print(random.dict, "    ", random.list)
print(random.remove(0), True)
print(random.dict, "    ", random.list)
print(random.insert(2), True)
print(random.dict, "    ", random.list)
print(random.remove(1), True)
print(random.dict, "    ", random.list)
print(random.getRandom(), "2")
