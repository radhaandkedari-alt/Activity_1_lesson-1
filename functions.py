def well_wishes():
    print("Hello, how r u?")
    print("Welcome to the Codingal")

well_wishes()

#assignment 1
def weather_conditions():
    print("The weather is pleasent", spring)
    print("The weather is same in ", autumn)

spring = "autumn"
autumn = spring

weather_conditions()

#assignment 2
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a/b

def mul(a, b):
    return a*b

a =int(input("Enter your first number:"))
b =int(input("Enter your second number:"))

c = add(a , b)
print("The value of c is:", c)

d = sub(a, b)
print("The value of d is:", d)

e = div(a, b)
print("The  value of e is:", e)

f = mul(a, b)
print("The value of f is:", f)

#create a function called calculate_total(price, quantity) 
#multiply price * quantity 
#return the total
#store the returned value into a variable
#print the result

def calculate_total(price, quantity):
    total = price * quantity
    return total

total_result = calculate_total(10, 5)
print("The total is:", total_result)


#difference between parameter and argument

#create a function square(number) that returns the square of a number
def square(number):
    return number * number

number = int(input("Enter a number to square: "))
result = square(number)
print("The square of", number, "is:", result)





