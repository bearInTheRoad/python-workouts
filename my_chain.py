def my_chain(*iterables):
    for iterable in iterables:
        for element in iterable:
            yield element


def my_zip(*iterables):
    iterators = [iter(iterable) for iterable in iterables]

    while True:
        try:
            # in PIP 479, StopIteration inside a generator
            # is no longer bubbling up and provide catch for
            # try except statement, it's now regarded as
            # a runtime error
            items = []
            for iterator in iterators:
                items.append(next(iterator))
            yield tuple(items)
        except StopIteration:
            # in geneartor function, return is the right way to
            # exit the loop
            return


for e in my_chain("abc", [1, 2, 3], {"a": 1, "b": 2}):
    print(e)

print(list(my_zip("abcdef", [1, 2, 3, 4, 5], [10, 20, 30])))
