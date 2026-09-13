class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = parrot("Blu", 10)
p2 = parrot("Woo", 15)
print("Blu is a:", p1.species)
print("Woo is also a:", p2.species)

print(p1.name, "is", p1.age, "years old")
print(p2.name, "is", p2.age, "years old")