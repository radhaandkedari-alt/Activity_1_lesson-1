class vehicle:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class bus(vehicle):
    pass 
bus1 = bus("School Van", 180, 12)
print(bus1.name, bus1.max_speed, bus1.milage)