class myclass:
    __private_variable = 27
    def __private_method(self):
        print("This is a private method.")

    def hello(self):
        print("Hello from myclass", myclass.__private_variable) 

my = myclass()

my.hello()  # This will work and print the private variable
my.__private_method()

