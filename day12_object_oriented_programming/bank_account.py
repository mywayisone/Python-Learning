# Create a class BankAccount with:

# - __init__ method that takes: owner_name, balance (default to 0).
# - deposit(amount) method to add money.
# - withdraw(amount) method to subtract if sufficient balance.
# - display_balance() method to print current balance.

# Bonus:
# - Prevent withdrawal of negative amounts or values greater than balance.
# - Add a method transfer_to(other_account, amount) to transfer money to another account.

class BankAccount:
    # Creating __init__() method
    def __init__(self, owner_name:str, balance = 0.0 ):
        self.name = owner_name
        self.balance = balance

    # Define deposit() method
    def deposit(self, amount: float):
        self.balance += amount

    # Define withdraw() method
    def withdraw(self, amount: float):
        if amount > 0:
            if amount > self.balance:
                self.balance -= amount
            else: print("Insufficient balance")
        else: print("Invalid amount")

    # Define display_balance() method
    def display_balance(self):
        print(f"Balance: {self.balance}")
    
    # Define transfer() method
    def transfer( self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
        else:print("insufficient balance")

    # Define account_info() method
    def account_info(self):
        print(f"Name: {self.name}\nBalance: {self.balance} ")

# Define main() function
def main():

    account1 = BankAccount("Matthew", 5000)
    account2 = BankAccount("Bunmi")
    account1.deposit(20000)
    account1.withdraw(1000)
    account1.account_info()
    account2.account_info()
    account1.transfer(account2, 10000)
    account2.account_info()
    account1.account_info()


if __name__ == "__main__":
    main()