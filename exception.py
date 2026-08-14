try: 
    number = int(input("Enter a number:"))
    result=100/number
except ValueError:
    print("Please enter a number") 
except ZeroDivisionError:
    print("you cannot divide by zero")
else:
    print("The result is:", result)
finally:
    print("Thank you, Program finished")

try:
    number=int(input("Enter a number:"))
    print("The number entered is:", number)
except ValueError as ex:
    print("exception", ex) 