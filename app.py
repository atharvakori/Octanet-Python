import datetime

user_data = {
    'name': 'Atharva Kori',
    'account_number': '1234567890',
    'pin': '1234',
    'balance': 5000.00,
    'transaction_history': []
}

# Function to display menu and get user choice
def display_menu():
    print("\nATM Simulator")
    print("1. Account Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. PIN Change")
    print("5. Transaction History")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

# Function to handle account balance inquiry
def check_balance():
    print(f"Your current balance is Rs {user_data['balance']:.2f}")

# Function to handle cash withdrawal
def withdraw_cash():
    amount = float(input("Enter the amount to withdraw: "))
    if amount > 0 and amount <= user_data['balance']:
        user_data['balance'] -= amount
        transaction = (datetime.datetime.now(), 'Withdrawal', amount)
        user_data['transaction_history'].append(transaction)
        print(f"Withdrawal successful. Remaining balance is Rs {user_data['balance']:.2f}")
    else:
        print("Invalid amount or insufficient balance.")

# Function to handle cash deposit
def deposit_cash():
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        user_data['balance'] += amount
        transaction = (datetime.datetime.now(), 'Deposit', amount)
        user_data['transaction_history'].append(transaction)
        print(f"Deposit successful. Current balance is Rs {user_data['balance']:.2f}")
    else:
        print("Invalid amount.")

# Function to handle PIN change
def change_pin():
    new_pin = input("Enter new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        user_data['pin'] = new_pin
        print("PIN changed successfully.")
    else:
        print("Invalid PIN. PIN must be a 4-digit number.")

# Function to display transaction history
def display_transaction_history():
    print("\nTransaction History:")
    for transaction in user_data['transaction_history']:
        print(f"{transaction[0]} - {transaction[1]} Rs {transaction[2]:.2f}")

# Main function to run the ATM simulator
def main():
    print("Welcome to the ATM")
    pin_attempts = 0
    while pin_attempts < 3:
        pin = input("Enter your 4-digit PIN: ")
        if pin == user_data['pin']:
            while True:
                choice = display_menu()
                if choice == '1':
                    check_balance()
                elif choice == '2':
                    withdraw_cash()
                elif choice == '3':
                    deposit_cash()
                elif choice == '4':
                    change_pin()
                elif choice == '5':
                    display_transaction_history()
                elif choice == '6':
                    print("Thank you for using the ATM. Goodbye!")
                    return
                else:
                    print("Invalid choice. Please enter a number from 1 to 6.")
        else:
            pin_attempts += 1
            print("Invalid PIN. Please try again.")
    print("Too many incorrect PIN attempts. Exiting...")

if __name__ == "__main__":
    main()
