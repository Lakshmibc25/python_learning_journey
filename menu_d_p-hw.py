def menu():
    print("---banking system---")
    print("1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. quit")

balance = 0
while(True):
    menu()
    choice = int(input ("enter your choice: "))
    if choice ==1 :
        print("Balance:", balance)
    elif choice == 2:
        amount = int(input("enter amount to deposit :"))
        balance += amount
        print("Balance: ", balance)
    elif choice == 3:
        amount = int(input("enter amount to withdraw: "))
        balance -= amount
        print("Balance: ", balance)
    elif choice == 4:
        print("thank you for using our banking system")
    break