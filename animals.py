class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return ",".join([self.species, self.color, str(self.number_of_legs)])


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class Cage:
    cage_created = []

    def __init__(self, id):
        if id in Cage.cage_created:
            raise Exception("The id already exists")
        self.id = id
        self.animals = []
        Cage.cage_created.append(id)

    def add_animals(self, *animals):
        for a in animals:
            self.animals.append(a)

    def __repr__(self) -> str:
        return f"{self.id} cage has {', '.join([animal.species for animal in self.animals])}"


class Zoo:
    def __init__(self) -> None:
        self.cages = []

    def add_cages(self, *cages):
        self.cages += cages

    def animals_by_color(self, color):
        return [
            animal
            for cage in self.cages
            for animal in cage.animals
            if animal.color == color
        ]

    def animals_by_legs(self, leg_count):
        return [
            animal
            for cage in self.cages
            for animal in cage.animals
            if animal.number_of_legs == leg_count
        ]

    def number_of_legs(self):
        return sum(
            (animal.number_of_legs for cage in self.cages for animal in cage.animals)
        )


wolf = Wolf("black")
sheep = Sheep("white")
snake = Snake("white")
parrot = Parrot("blue")

c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)

print(c1)
print(c2)
print(c2.cage_created)

z = Zoo()
z.add_cages(c1, c2)
print(z.animals_by_color("white"))
print(z.animals_by_legs(4))
print(z.number_of_legs())
