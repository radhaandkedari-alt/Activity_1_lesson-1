class computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

comp = computer()
comp.sell()
comp.__maxprice = 1000  # This will not change the private variable
comp.sell()
