#create a class called book with attributes title, author, and price. Create 3 book objects and print their details
class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = book("Percy Jackson", "Rick Riordan", 9.99)
book2 = book("The Hunger Games", "suzanne Collins", 12.99)
book3 = book("Powerless", "Lauren Roberts", 10.99)

print("Book 1: Title:", book1.title, ", Author:", book1.author, ", Price:", book1.price)
print("Book 2: Title:", book2.title, ", Author:", book2.author, ", Price:", book2.price)
print("Book 3: Title:", book3.title, ", Author:", book3.author, ", Price:", book3.price)