#Assignment 1

tree1=98

tree2=76

tree3=89

tree4=11

tree5=95

#Finding the total of tree

sum=tree1+tree2+tree3+tree4+tree5

print("The total number of trees is:", sum)

# finding teh average of trees

average=sum/5

print("The average number of trees is:", average)

amount=int(input("please enter amount for withdraw"))
note_1=amount//100
note_2=(amount %100)//50
note_3=((amount %100)%50)//10

print("notes of 100 rupees", note_1)
print("notes of 50 rupees", note_2)
print("notes fo 10 rupees", note_3)