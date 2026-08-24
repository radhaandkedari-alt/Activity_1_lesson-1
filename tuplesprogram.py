tuplex=("tuple", False, 3.2, 1)
print("The Value of tuplex is:", tuplex)

tuplex=(4, 6, 2, 8, 3, 1)
print(tuplex) #tuples are immutable, so u cannot add new elements, and if u want to add, use the plus operator sign
a=tuplex+(9,)
print("The value after addition:", a)
tuple1=(50, 10, 60, 70, 50)
print(tuple1.count(50))

slice=tuple1[1:3]
print("The value of slice is:", slice)

slice1=tuple1[:4]
print("The value of the slice1 is:", slice1)

student=("uma", 20, 85.5, "delhi")
slice2=student[:3]
print(slice2)

#assignment 2
colors=("blue", "red", "red", "yellow", "red")
print(colors.count("red"))