balance = 1000

while True:
    print("\n--- ATM MENU ---")
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        while True:
            amount = int(input("Deposit (50/100/200/500) or 0 to cancel: "))
            if amount == 0:
                break
            if amount in [50, 100, 200, 500]:
                balance += amount
                print("New balance:", balance)
                break
            else:
                print("Invalid amount")

    elif choice == "3":
        while True:
            amount = int(input("Withdraw (50/100/200/500) or 0 to cancel: "))
            if amount == 0:
                break
            if amount in [50, 100, 200, 500]:
                if amount <= balance:
                    balance -= amount
                    print("New balance:", balance)
                else:
                    print("Insufficient funds")
                break
            else:
                print("Invalid amount")

    elif choice == "0":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
