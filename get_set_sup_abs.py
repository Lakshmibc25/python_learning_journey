class BankAccount:
   def __init__(self,balance):
      if balance >= 0:
       self.__balance = balance
      else:
        self.__balance = 0
   def get_balance(self):
     return self.__balance
   
   def set_balance(self,amount):
     return self.__balance

account = BankAccount(100)
print(account.get_balance())

account.set_balance(50)
print(account.get_balance())


print(account.get_balance())
   
      