class student:
    grade = 10
    print("Hi, I am a student of grade", grade)

ob = student()

#assignment 2
class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

a = Vehicle(200, 10)
print("Max speed is:", a.max_speed)
print("Milage is:", a.milage)
