#if while loop is used to repeat a block of code again and again as long as a conditon is true
#when do we use while loop?
#we use a while loop when we dont know exactly how many times the code should repeat
#examples: the first one is keep asking for correct password until correct. secon: keep playing until the game over. third: keep adding numbers until user types 0.
#why do we use while loop?
#when do we use while loop
#without a loop
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
count=1

while count<=5:
    print("hello")
    count+=1
#tricks to remember while loop
#CDUR
#C - Create a variable to control the loop
#D - Define the condition for the loop
#U - Update the variable inside the loop
#R - Repeat the process

#assignment no1
sum=0
i=0
while i<=0:
    print("hello, how r u?")
    i=i+1

#find the odd or even number
num=int(input("please enter a number:"))
while num>0:
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")
