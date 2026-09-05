numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print("The value of result is:", result.__next__())
print(list(result))

nums = [1, 2, 3, 4, 5]
def square(x):
    return x * x
squared_nums = list(map(square, nums))
print(squared_nums)

#create a list using range

