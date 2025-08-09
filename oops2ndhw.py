class employee:
    
    def __init__(self,name,designation,salary=30000):
        self.name = name
        self.designation = designation
        self.salary = salary
    def emp_info(self):
        print(f"name : {self.name}, designation :{self.designation}, salary: {self.salary}")

employee1 = employee("lakshmi","hr",90000)
employee2 = employee("harshitha","head",80000)
employee3 = employee("kavitha","maneger")

employee1.emp_info()
employee2.emp_info()
employee3.emp_info()



