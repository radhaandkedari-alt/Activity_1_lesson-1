string=input("Please enter your own word:")

character=input("Please enter your own character:")

i = 0
count = 0


while i < len(string):
    if string[i] == character:
        count+=1
    i=i+1   
print("The character",character,"is present in the string",string,"for",count,"times")   