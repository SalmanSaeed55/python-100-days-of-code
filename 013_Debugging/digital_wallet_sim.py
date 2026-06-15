def transaction(action_type, amount, storage):
    storage.append([action_type, f"{int(amount):.2f}"])


def deposit(current_balance, storage):
    while True:
        try:
            deposit_amount = int(input("Enter deposit amount: "))

            if deposit_amount > 0:
                current_balance += deposit_amount
                transaction("Deposit", deposit_amount, storage)
                print(f"Deposited: £{deposit_amount:.2f}")
                print(f"New Balance: £{current_balance:.2f}\n")
                return current_balance
            else:
                print("Deposit amount must be greater than 0.\n")
        except ValueError:
            print("Please enter a valid number.\n")


def withdraw(current_balance, storage):
    while True:
        try:
            withdraw_amount = int(input("Enter withdraw amount: "))

            if current_balance >= withdraw_amount > 0:
                current_balance -= withdraw_amount
                transaction("Withdraw", withdraw_amount, storage)
                print(f"Withdrew: £{withdraw_amount:.2f}")
                print(f"New Balance: £{current_balance:.2f}\n")
                return current_balance
            elif withdraw_amount <= 0:
                print("Withdraw amount must be greater than 0.\n")
            else:
                print("Insufficient funds for this withdrawal.\n")
        except ValueError:
            print("Please enter a valid number.\n")


def view_transactions(storage):
    for i in range(len(storage)):
        print(f"{i + 1}. {storage[i][0]} \t £{storage[i][1]}")


def main_menu():
    while True:
        try:
            options = int(input("""What would you like to do?
             1. Check Balance
             2. Deposit
             3. Withdraw
             4. View transaction history
             5. Exit\n\t>"""))

            if 1 <= options <= 5:
                break
            else:
                print("Out of bounds. Please enter a number from 1 to 4.\n")
        except ValueError:
            print("Please enter a valid option (1-5).")

    print(f"Preparing with option {options}")
    return options


transaction_history = []
balance = 150
transaction("Initial Balance", balance, transaction_history)


if __name__ == '__main__':
    print("Welcome to Your Digital Wallet\n")
    print("Starting Balance: \t £150.00\n")

    while True:
        choice = main_menu()
        if choice == 1:
            print(f"Current Balance: \t £{balance:.2f}")
        elif choice == 2:
            balance = deposit(balance, transaction_history)
        elif choice == 3:
            balance = withdraw(balance, transaction_history)
        elif choice == 4:
            view_transactions(transaction_history)
        elif choice == 5:
            print("Exiting the digital wallet. Goodbye!")
            break
