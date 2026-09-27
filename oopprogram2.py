class employee:
    def __init__(self):
        print("Employee class constructor called")
    def __del__(self):
        print("Employee class destructor called")

def create_object():
    print("Creating employee object")
    emp = employee()
    print("Employee object created")
    return emp

print("Calling create_object function")
emp1 = create_object()

print("Program end")