# Problem statement in description

class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.min_balance = 1000

    def withdraw(self, amt):
        if self.balance - amt < self.min_balance:
            print("Insufficient balance")
        else:
            self.balance -= amt

    def deposit(self, amt):
        if amt < 0:
            print("Invalid Amount")
        else:
            self.balance += amt

    def display_balance(self):
        print("Balance = ", self.balance)

def main_menu():
    atm = ATM(10000)

    while True:
        print("1. Display Balance")
        print("2. Withdraw Amount")
        print("3. Deposit Amount")
        print("4. Quit")

        choice = int(input("Enter choice [1-4]: "))

        if choice == 1:
            atm.display_balance()
        elif choice == 2:
            amt = int(input("Enter amount to withdraw: "))
            atm.withdraw(amt)
        elif choice == 3:
            amt = int(input("Enter amount to deposit: "))
            atm.deposit(amt)
        elif choice == 4:
            break
        else:
            print("Invalid choice")

main_menu()

