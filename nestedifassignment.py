age=int(input("please enter your age"))
ticket=input("do you have a ticket? yes/no:")

if age>=19:
    if ticket=="yes":
        print("enjoy the movie")
    else:
        print("please buy a ticket")
else:
    print("sorry you are too young")
