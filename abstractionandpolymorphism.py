from abc import ABC, abstractmethod      #abstract base class

class Animal(ABC):
    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk and run")

class snake(Animal):
    def move(self):
        print("I can crawl")

class dog(Animal):
    def move(self):
        print("I can bark")

class lion(Animal):
    def move(self):
        print("I can roar")

human1 = human()
human1.move()
snake1 = snake()
snake1.move()
dog1 = dog()
dog1.move()
lion1 = lion()
lion1.move()