#server.py
import Pyro4
@Pyro4.expose
class Bank:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        self.balance += amount
        return f"Deposit successful. Balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawal successful. Balance: {self.balance}"

    def check_balance(self):
        return self.balance
daemon = Pyro4.Daemon()
uri = daemon.register(Bank())
print("Bank server is running")
print("Server URI:", uri)
daemon.requestLoop()

#client.py

import Pyro4

uri = input("Enter Server URI: ")
bank = Pyro4.Proxy(uri)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        print(bank.deposit(amount))
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        print(bank.withdraw(amount))
    elif choice == "3":
        print("Balance:", bank.check_balance())
    elif choice == "4":
        bank._pyroRelease()
        break
    else:
        print("Invalid choice")
