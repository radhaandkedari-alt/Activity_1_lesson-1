class dog():
    def sound(self):
        print("bark")

class cat():
    def sound(self):
        print("meow")

dog1 = dog()
cat1 = cat()

for animal in(dog1, cat1):
    animal.sound()