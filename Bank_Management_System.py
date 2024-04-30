
# Account class
class Account:
    def __init__(self,password,name,email,address,account_type):
        self.password = password
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_balance = 0
        self.transactions = []
        self.loan_take = 0
        
    
    
    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(f"Deposited ${amount}")
        print("Deposit successful.")
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            self.transactions.append(f"Withdraw ${amount}")
            print("Withdraw successful.")
        else:
            print("!Withdraw amount exceeded.!")
            
    def execute_transaction(self,transaction_type,amount):
        if transaction_type == "deposite":
            self.deposit(amount)
        elif transaction_type == "withdraw":
            self.withdraw(amount)
        else:
            print("!Invalid transaction type.!")
            
    def check_balance(self):
        print(f"Your account balance is {self.balance}.")
        
    def check_loan(self):
        print(f"Your loan balance is {self.loan_balance}.")
    
    def transaction_history(self):
        count = 1
        for tranaction in self.transactions:
            print(f"{count}.{tranaction}")
            count += 1
            
    def take_loan(self,amount):
        if self.loan_take < 2:
            if bank.loan_feature:
                if bank.available_balance() > amount:
                    self.balance += amount
                    self.loan_take -= 1
                    self.loan_balance += amount
                    self.transactions.append(f"Loan taken &{amount}")
                    print("Loan taken successfully.")
                else:
                    print("!The bank is bankrupt!")
            else:
                print("!Loan feature is currently disabled by admin.!")
        else:
            print("!You have already taken maximun number of loans.!")
            
    def return_loan(self,amount):   
        if self.balance >= amount:
            if self.loan_balance > 0 and amount <= self.loan_balance:
                self.balance -= amount
                self.loan_take += 1
                if self.loan_take > 2:
                    self.loan_take = 2
                self.loan_balance -= amount
                self.transactions.append(f"Loan returned ${amount}")
                print("Loan return successfully.")
            elif self.loan_balance > 0 and amount > self.loan_balance:
                self.balance -= self.loan_balance
                self.loan_take += 1
                if self.loan_take > 2:
                    self.loan_take = 2
                self.transactions.append(f"Loan returned ${self.loan_balance}")
                self.loan_balance = 0
            elif self.loan_balance <= 0:
                print("You don't have any loan")
        else:
            print("!Insufficient balance to return loan.!")
        
    
            
    def transfer(self,receiver_number,account_number,amount,bank):
        if receiver_number in bank.users:
            receiver = bank.users[receiver_number]
            if self.balance >= amount:
                self.balance -= amount
                receiver.balance += amount
                self.transactions.append(f"Transfer ${amount} to account {receiver_number}")
                receiver.transactions.append(f"Transfer ${amount} from account {account_number}")
                print("Transfer successful")
            else:
                print("Insufficient balance to transfer.")
        else:
            print("!Receiver account number is invalid!")
    
# Bank class
class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan = 0
        self.total_available_balance = 0
        self.loan_feature = True
        self.count = 1000000
    def create_account(self,password,name,email,address,account_type):
        account = Account(password,name,email,address,account_type)
        account_number = self.count
        self.count += 1
        self.users[account_number] = account
        print(f"Account created successfully.\n Your account number is {account_number}")
        
    def delete_account(self,account_number):
        if account_number in self.users:
            del self.users[account_number]
            print("Account delete successfully.")
        else:
            print("Account does not exist")
            
    def get_all_account(self):
        print("name\t\taccounttype\taccount number")
        for account_number,user in self.users.items():
            print(f"{user.name}\t\t{user.account_type}\t\t{account_number}")
    
    def get_total_balance(self):
        self.total_balance = 0
        for user in self.users.values():
            self.total_balance += user.balance 
        return (self.total_balance)
    
    def get_total_loan(self):  
        self.total_loan = 0
        for user in self.users.values():
            self.total_loan += user.loan_balance 
        return (self.total_loan)
        
    def available_balance(self):   
        self.total_available_balance = 0
        self.total_available_balance = self.get_total_balance() - self.get_total_loan()
        return self.total_available_balance
        
    def toggle_loan_feature(self,status):
        self.loan_feature = status
        if status:
            print("Loan feature is enabled.")
        else:
            print("Loan feature is disabled.")



    
def restration(bank):
    name = input("Enter Your name : ")
    email = input("Enter Your email : ")
    address = input("Enter your address :")
    account_type = "Other"
    print("Choice your account type -")
    print("1. Savings ")
    print("2. Cuurent ")
    choice = input("Enter type: ")
    if choice == "1":
        account_type = "Savings"
    elif choice == "2":
        account_type = "Cuurent"
    password = input("Enter a password : ")
    bank.create_account(password,name,email,address,account_type)
    
def user_login(bank):
    account_number = int(input("Enter your account number : "))
    password = input("Enter a password : ")
    if account_number in bank.users:
        if password == bank.users[account_number].password:
            return bank.users[account_number]
        else:
            print("Password is wrong")
            return None
    else:
        print("Invalid account number")
        return None
    
def admin_login():
    username = input("Enter admin username : ")
    password = input("Enter admin password : ")
    if username == "admin" and password == "admin":
        return True
    else:
        print("Invalid admin username & password")
        return False
    
bank = Bank()

while True:
    print("""
          -----------------------------------------
          | Welcome to the bank management system |
          -----------------------------------------
            """)
    print()
    print("1. Registration & Create Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")
    print()
    choice = input("Enter your choice : ")
    if choice == "1":
        restration(bank)
    elif choice == "2":
        user = user_login(bank)
        if user:
            while True:
                print("""
                      ---------------
                      |  User Menu  |
                      ---------------
                      """)
                print()
                print("1. Execute Trasaction(Deposit or Withdraw)")
                print("2. Check Balance")
                print("3. Transfer Balance to Another Account")
                print("4. Take Loan")
                print("5. Transaction History")
                print("6. Return Loan")
                print("7. Check Loan Amount")
                print("8. Logout")
                print()
                user_choice = input("Enter your choice : ")
                if user_choice == "1":
                    print("Choice your transaction type -")
                    print("1. deposit ")
                    print("2. withdraw ")
                    c = input("Enter type: ")
                    if c == "1":
                        transaction_type = "deposite"
                    elif c == "2":
                        transaction_type = "withdraw"
                    amount = int(input("Enter amount : "))
                    user.execute_transaction(transaction_type,amount)
                elif user_choice == "2":
                    user.check_balance()
                elif user_choice == "3":
                    receiver_number = int(input("Enter receiver number : "))
                    account_number = int(input("Enter your account number : "))
                    amount = int(input("Enter amount to transfer : "))
                    user.transfer(receiver_number,account_number,amount,bank)
                elif user_choice == "4":
                    amount = int(input("Enter loan amount : "))
                    user.take_loan(amount)
                elif user_choice == "5":
                    user.transaction_history()
                elif user_choice == "6":
                    amount = int(input("Enter amount to return loan : "))
                    user.return_loan(amount)
                elif user_choice == "7":
                    user.check_loan()
                elif user_choice == "8":
                    break
                else:
                    print("Invalid choice.")
                  
    elif choice == "3":
        if admin_login():
            while True:
                print()
                print("""
                      -----------------
                      |  Admin Menu   |
                      -----------------
                      """)
                print()
                print("1. Create Account")
                print("2. Delete Account")
                print("3. See All User List")
                print("4. See Total Balance of Bank")
                print("5. See Total Loan")
                print("6. Toggle loan Feature")
                print("7. Logout")
                print()
                
                admin_choice = input("Enter your choice : ")
                if admin_choice == "1":
                    restration(bank)
                elif admin_choice == "2":
                    account_number = int(input("Enter account number to delete : "))
                    bank.delete_account(account_number)
                elif admin_choice == "3":
                    print("All user list : ")
                    print()
                    bank.get_all_account()
                elif admin_choice == "4":
                    print("Total avaliable balance : ",bank.available_balance())
                elif admin_choice == "5":
                    print("Total loan : ",bank.get_total_loan())
                elif admin_choice == "6":
                    print("Choice Status ")
                    print("1. True ")
                    print("2. False ")
                    status = True
                    c = input("Enter type: ")
                    if c == "1":
                        status = True
                    elif c == "2":
                        status = False
                    bank.toggle_loan_feature(status)
                elif admin_choice == "7":
                    break
                else:
                    print("Invalid choice.")
                    
    elif choice == "4":
        print("Exit")
        print()
    else:
        print("Invalid choice.")
