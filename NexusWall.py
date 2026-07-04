from abc import ABC, abstractmethod
class Transaction(ABC):
    def __init__(self,name,funds):
        self.name=name
        self._funds=funds
    def display_status(self):
        if self._funds>0:
            print(f"Sender's name:{self.name}|Fund amount:{self._funds}") 
        else:
            print(f"Error:{self.name} has to enter or have certain money to enter transactions")
    @abstractmethod
    def authorize(self):
        pass
class InstitutionalTransfer(Transaction):
    def authorize(self):
        if self._funds>=50000:
          print(f"Premium transaction of {self.name} is SECURED ")
        else:
          print(f"Premium transaction of {self.name} is on HOLD (Elite Threshold Failed)")    
Transaction_A=InstitutionalTransfer("Alex",5000)
Transaction_A.display_status()
Transaction_A.authorize()
print("-------------------")
Transaction_B=InstitutionalTransfer("Zack",200000)
Transaction_B.display_status()
Transaction_B.authorize()
print("-------------------")