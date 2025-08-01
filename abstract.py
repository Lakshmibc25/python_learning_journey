from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class bike(vehicle):
    def __init__(self,name):
        self.name = name
    
    def start_engine(self):
        print("start_engine")

b = bike("royal enfiled")
print(b.name)