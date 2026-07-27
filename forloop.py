a = int(input("enter the number whose sum you want to find:"))
sum=0
#iterating for a+1 times: i = 1 to a+1

for i in range(1,a+1):
    sum=sum+i
print("the sum", sum)

#assignment 2
#input a word or sentence 
string=input("please enter your own string:")
string2=("")

#loop for printing in reverse
for i in string:
    string2=i+string2

print("the original string is:", string)
print("the reversed string is:", string2)