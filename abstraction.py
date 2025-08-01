class ATM:
    def __init__(self, balance):
        self.__balance = balance
    def check_balance(self):
        print(self.__balance)

pnb = ATM(100000)

print(pnb.__balance)
