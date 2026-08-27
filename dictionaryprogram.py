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
    "id3": {"name":"sara",
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
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details