empty_list=[]
print()

numbers=[1, 2, 3, 4, 5]
print(numbers)

triples=[1, 2, 3] * 3
print("The value of the triples", triples)

triples=triples[::-1] #list slicing list[start : stop : step]
print(triples) 

#list program 2.py
def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    return ctr

count = match_words(["abc", "cfc", "xyz", "aba", "1221"])
print("The number of words having first and last character", count)  
          