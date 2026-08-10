def total_calc(bill_amount,tip_perc):

#define function to calculate the tip on bill
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")

# specify only bill_amount

# default value of tip percentage is used

total_calc(150,20)

def cube(number):
    return number*number*number

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

output=by_three(9)

print(by_three(9))


def factorial(x):
    """ this a recursive function to find teh factorial of an number """

    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
