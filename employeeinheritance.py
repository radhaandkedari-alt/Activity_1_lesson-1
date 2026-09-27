class person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name, self.idnumber)

class employee(person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post
employee1 = employee("John", 886012, 20000, "Intern")
employee1.display()