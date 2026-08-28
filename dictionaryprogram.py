bag={
    "books":5, 
    "pencils":3,
    "erasers":2
}

for item, quantity in bag.items():
    print(item, quantity)

bag.pop("books")
print("After pop up, the value of bag is:", bag)

marks={
    "math":90,
    "english":85,
    "science":95
}

for subject in marks:
    print(subject)

for subject, marks in marks.items():
    print(subject, marks)

student_data={
    "id1": {"name":"sara",
            "subject": "english,math,science",
            "class": 5
            },
    "id2": {"name":"sara",
            "subject": "english,math,science",
            "class": 5
            },
    "id3": {"name":"uma",
            "subject": "english,math,science",
            "class": 5
            }
}

seen_keys=[]
result={}
for student_id,details in student_data.items():
    print(student_id, details)
    unique_key=(details["name"],
                details["subject"],
                details["class"]
                )
    print("The value of unique_key:", unique_key)
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details

for k,v in result.items():
    print("The value of key and value is:", k, ":", v)



#homework
#create a dictionary called student with name, age, class and you need to print it
student = {
    "name": "John",
    "age": 10,
    "class": 5
}
print(student)

#homework 2
#print both the keys and value using a for loop
for key, value in student.items():
    print(key, value)


#homework 3
#using the same dictionary print only the student's name
print(student["name"])

#homework 4
#change the student age from 10 to 11
student["age"] = 11

print(student)

#assignemnt 
student={
    "id1": "sara",
    "id2": "david",
    "id3": "sara",
    "id4": "john"
}

result={}
seen_keys=[]
for student,details in student.items():
    print("The value of student:", student, details)

    if details not in seen_keys: 
        seen_keys.append(details)
        result[student]=details

for k, v in result.items():
     print(k, ":", v)

#assignment
marks={
    "sara": 85,
    "david": 90,
    "john": 78
    }