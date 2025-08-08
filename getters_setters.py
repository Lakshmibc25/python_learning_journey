class student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self):
        return self.__name
    
    def set_age(self,age):
        if isinstance(age,int):
          self.__age = age
        else:
             print("age should be an int.error,try again")

s = student("lakshmi",19)

s.set_age (100)

