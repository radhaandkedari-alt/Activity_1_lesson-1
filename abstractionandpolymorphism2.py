class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Washington DC is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")

india1 = India()
usa1 = USA()

#common interface
for country in (india1, usa1):
    country.capital()
    country.language()
    country.type()