class Circle:
    def __init__(self, iterable, times):
        self.iterable = iterable
        self.times = times

    def __iter__(self):
        return _Circle(self.iterable, self.times)


class _Circle:
    def __init__(self, iterable, times):
        self.iterable = iterable
        self.times = times
        self.counter = 0

    def __next__(self):
        while self.counter < self.times:
            index = self.counter
            self.counter += 1
            return self.iterable[index % len(self.iterable)]
        raise StopIteration

    def __iter__(self):
        return self


def my_cicrle(sequence, times):
    counter = 0
    while counter < times:
        yield sequence[counter % len(sequence)]
        counter += 1


c = my_cicrle("abc", 5)
# for element in c:
#     print(element)
print(list(c))  # a,b,c,a,b
