import array as arr

my_set={1, 2, 3}
print("The value of my set is:", my_set)

my_set1={1.0, "hello", (1, 2, 3)}
print("The value of my_set1 is:", my_set1)

my_set2={1, 2, 3, 4, 3, 2}
print("The value of my_set2 is:", my_set2)

list1=[1, 2, 3, 2]
print("the value of the list1 is:", list1)

my_set3=set(list1)
print("The value of my_set3 is:", my_set3)

#remove a number from a set
print("The value after remove", my_set3.pop())
print("The final value after removing:", my_set3)

#assignment 2
array_num=arr.array('i', [2, 5, 2, 8, 2, 9, 4])
print(str(array_num.count(2)))