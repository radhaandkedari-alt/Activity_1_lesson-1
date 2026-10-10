from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    def profit(self):
        pass

class ICICI(Bank):
    def interest(self):
        return 5.0

sbi1 = SBI()
icici1 = ICICI()

for bank in (sbi1, icici1):
    print(bank.interest())
