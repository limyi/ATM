class Account:
    def __init__(self, pin, initial_balance=0):
        self.pin = pin
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

class ATM:
    def __init__(self):
        self.current_account = None

    def insert_card(self, card_number, pin):
        # Assume you have a list of valid card numbers and their associated PINs.
        # Check if the card number and PIN are valid.
        if self.is_valid_card(card_number, pin):
            self.current_account = Account(pin)

    def is_valid_card(self, card_number, pin):
        # Replace this with your card validation logic.
        # You might want to store card numbers and PINs in a database or file.
        valid_card_numbers = ['1234567890123456', '9876543210987654']
        valid_pins = ['123456', '654321']

        return card_number in valid_card_numbers and pin in valid_pins

    def select_account_type(self):
        if self.current_account:
            while True:
                account_type = input("Select account type (1. Savings, 2. Checking): ")
                if account_type in ['1', '2']:
                    return int(account_type)
                else:
                    print("Invalid account type. Please select 1 or 2.")

    def main_menu(self):
        if self.current_account:
            while True:
                print("\nMain Menu:")
                print("1. See Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")

                choice = input("Enter your choice: ")
                if choice == '1':
                    balance = self.current_account.get_balance()
                    print(f"Current balance: ${balance}")
                elif choice == '2':
                    amount = float(input("Enter the deposit amount: $"))
                    if self.current_account.deposit(amount):
                        print("Deposit successful.")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3':
                    amount = float(input("Enter the withdrawal amount: $"))
                    if self.current_account.withdraw(amount):
                        print("Withdrawal successful.")
                    else:
                        print("Invalid withdrawal amount.")
                elif choice == '4':
                    print("Thank you for using the ATM. Goodbye!")
                    self.current_account = None
                    break
                else:
                    print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm = ATM()

    while True:
        card_number = input("Enter your card number: ")
        pin = input("Enter your 6-digit PIN: ")

        atm.insert_card(card_number, pin)

        if atm.current_account:
            account_type = atm.select_account_type()
            print(f"Welcome to your {'Savings' if account_type == 1 else 'Checking'} account!")
            atm.main_menu()
        else:
            print("Invalid card number or PIN. Please try again.")
