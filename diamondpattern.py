rowsize=int(input("Enter the number of rows you want to print:"))
#rowsize=5

if rowsize%2==0: #% gives you teh remainder
    halfDimRow=rowsize//2 # chcek teh quotient value and whaever teh value vefre decimal tyou need to ick

#it up
else:
    halfDimRow=rowsize//2+1 # 3

#upper
#Row 1
#Row 2
#Row 3

#lower
#row 4
#row 5


#upeper rowsize is 3

    space=halfDimRow-1

for i in range(1,halfDimRow+1): # thsi loop print rows

#runs
#1
#2
#3

    for j in range(1, space+1):
        print(end=" ")
        space=space-1 # space--
        num=1
    for j in range(2*i-1): # 2*1-1=1
        print(j, end="")
        num=num+1

if rowsize % 2 == 0:
    halfDimRow = rowsize // 2
    lower_start = halfDimRow
else:
    halfDimRow = rowsize // 2 + 1
    lower_start = halfDimRow - 1

for i in range(1, halfDimRow + 1):
    print(" " * (halfDimRow - i) + "".join(str(n) for n in range(1, 2 * i)))

for i in range(lower_start, 0, -1):
    print(" " * (halfDimRow - i) + "".join(str(n) for n in range(1, 2 * i)))