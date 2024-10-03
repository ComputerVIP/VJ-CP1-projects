#Vincent Johnson What's Goin On Here assignment

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        #Turns the account into the variable self

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    #This just adds to the amount in your account

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    #This function is just checking if your account has enough money

    def get_balance(self):
        return self.balance

def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)
    #Only works if def main() choice was 1

def main():
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
            #This is how it makes an account, gives it a number, and a starting value
        
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ")
            #This just checks to see if there is an account
            if account_number in accounts:
                #If account number is in accounts:
                account = accounts[account_number]
                if choice == '2':
                    #If they picked 2 then it allows them to deposit money
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                        #If it works, prints the amount deposited correctly
                    else:
                        print("Invalid deposit amount.")
                        #Only goes here if it doesn't work depositing
                elif choice == '3':
                    #If they picked 3 it allows them to withdraw
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        #If it works, withdraws the amount correctly
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                        #If it doesn't work it goes here, withdraw failed
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
                    #This just prints out your balance if you didn't pick 1-3
            else:
                print("Account not found.")
                #This is if your account is not in the system
        
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        #This is if they entered 5 to stop the program
        
        else:
            print("Invalid choice. Please try again.")
    #This function is the housing, the hub where you can access the other functions

if __name__ == "__main__":
    main()
    #This just runs main()