class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):      #lt is less than

        if (self.a < other.a):
            return "Ob1 is less than Ob2"
        else:
            return "Ob1 is not less than Ob2"

    def __eq__(self, other):      #eq is equal to
        if (self.a == other.a):
            return "Ob1 is equal to Ob2"
        else:
            return "Ob1 is not equal to Ob2"

obj1 = A(2)
obj2 = A(3)
print(obj1 < obj2)  # calls __lt__ method
print(obj1 == obj2) # calls __eq__ method