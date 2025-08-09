def menu():
    print("1. cart.")
    print("2. remove.")
    print("3. price.")
    print("4. exit.")

price = 0
while True:
    menu()
    choice = int(input("enter your choice: "))
    if choice ==1:
        print(str(input("enter items to add cart , price:")))
    elif choice == 2:
        print(str(input("enter items that has to be removed,price:")))
    elif choice == 3:
        price = (int(input("enter all the prices:")))
        total_price =+ price
        print(total_price)
    elif choice == 4:
        print("exiting..")
        break
    else:
       print("invalid input")
    