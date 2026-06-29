class FlexibleDict(dict):
    def __init__(self):
        super().__init__()

    def __getitem__(self, key):
        try:
            return super().__getitem__(str(key))

        except KeyError:
            return super().__getitem__(int(key))


fd = FlexibleDict()

fd["a"] = 100
print(fd["a"])
fd[5] = 500
print(fd[5])
print(fd["5"])
