num=3
if num>0:
    print("The number is positive")
num=-1
if num>0:
    print("The number1 is positive")

    #assignment 2
actual_cost=float(input("plese enter the acutal product price"))
sale_amount=float(input("please enter the sales amount"))

if sale_amount>actual_cost:
    amount= sale_amount-actual_cost
    print("the total profit", amount)
else: 
    print("no profit")
    
#assignment 3
num1=int(input("please enter your first number"))
if num1%2==0:
    print("the number is even")
else:
    print("the number is odd")

#assignment 5
name=input("please enter ur name")
if name=="uma":
    print("you are allowed to enter the school")
else:
    print("you are not allowed to enter the school")

#assignment 6
name=input("please enter your name")
age=int(input("please enter your age"))
if age>=16 and name=="uma":
    print("you are allowed to enter the school")
else:
    print("you are not allowed to enter the school")

#assignment 7
a=10
b=12
c=0

if a and b and c:
    print("all the numbers have boolean value as true")

elif a>0 or b>0:
    print("either of the number is greater than 0")

elif b>0 or c==0:
    print("uma either of the number is greater than 0")

else:
    print("all the numbers have boolean value as false")

#assignment 8
a=10
b=12
c=12
print(not(a==b))












