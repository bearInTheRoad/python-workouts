def my_enumerate(iterable):
    i = 0
    for element in iter(iterable):
        yield (i, element)
        i += 1


class MyEnumerate:
    def __init__(self, iterable) -> None:
        self.iterable = iterable

    def __iter__(self):
        return _MyEnumerate(self.iterable)


class _MyEnumerate:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.index = 0

    def __next__(self):
        index = self.index
        value = next(self.iterable)
        self.index += 1
        return index, value

    def __iter__(self):
        return self


word_list = ["this", "is", "a", "list", "of", "words"]
for index, word in MyEnumerate(word_list):
    print(f"{index}: {word}")
