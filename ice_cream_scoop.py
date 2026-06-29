class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return self.flavor


def create_scoops():
    return [Scoop("chocolate"), Scoop("vanilla"), Scoop("persimmon")]


# print(create_scoops())


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def __repr__(self):
        return ",".join((scoop.flavor for scoop in self.scoops))

    def add_scoops(self, *inputs):
        print(self.max_scoops)
        for input in inputs:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(input)


class BigBowl(Bowl):
    max_scoops = 5


s1 = Scoop("chocolate")
s2 = Scoop("vanilla")
s3 = Scoop("persimmon")

b = BigBowl()
b.add_scoops(s1, s2)
b.add_scoops(s3, s2, s1)
print(b)
