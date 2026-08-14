a = input("Enter a word:")
for i in a:
    if i == 'a':
        print("a is found")
        break
    else:
        print("a is not found")

#assignment 2
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print("Current variable value:", var)
    
#assignment 3
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

#assignment 4
food = ["burger", "salad", "fries", "pizza", "rice"]
for i in food:
    if i == "fries" or i == "burger" or i == "pizza":
        continue
    print(i)

#assignment 5
def check_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
age = int(input("enter your age:"))
result = check_age(age)
print(result)

#assignment 6: adding 2 numbers
def add_numbers(num1,num2):
    return num1 + num2
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
result = add_numbers(num1, num2)
print("The sum is:", result)
