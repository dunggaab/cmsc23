from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def balanceInformation(self)-> str:
        pass
    @abstractmethod
    def accountInformation(self)-> str:
        pass

## DEBIT MINIMUM = 100
## CREDIT MAXIMUM = 1,000,000


class Payroll(BankAccount):
    def __init__(self, accountNumber:int, accountOwner:str, balance: float, status: str):
        self.__accountNumber = accountNumber
        self.__accountOwner = accountOwner
        self.balance= balance
        self.status = status
    def balanceInformation(self)-> str:
        return  "Balance: " + str(self.balance)       
    def accountInformation(self)-> str:
        return "Account Information: \nAccount Type: Payroll\nAccount Number: " + str(self.__accountNumber) + "\nAccount Name: " + self.__accountOwner + "\nAccount Status: " + self.status

class Debit(BankAccount):
    def __init__(self, accountNumber:int, accountOwner:str, balance: float, status: str):
        self.__accountNumber = accountNumber
        self.__accountOwner = accountOwner
        self.balance= balance
        self.status = status
    def balanceInformation(self)-> str:
        return  "Balance: " + str(self.balance)       
    def accountInformation(self)-> str:
        return "Account Information: \nAccount Type: Payroll\nAccount Number: " + str(self.__accountNumber) + "\nAccount Name: " + self.__accountOwner + "\nAccount Status: " + self.status

class Credit(BankAccount):
    def __init__(self, accountNumber:int, accountOwner:str, balance: float, status: str):
        self.__accountNumber = accountNumber
        self.__accountOwner = accountOwner
        self.balance= balance
        self.status = status
    def balanceInformation(self)-> str:
        return  "Credit Balance: " + str(self.balance)       
    def accountInformation(self)-> str:
        return "Account Information: \nAccount Type: Payroll\nAccount Number: " + str(self.__accountNumber) + "\nAccount Name: " + self.__accountOwner + "\nAccount Status: " + self.status

class BankingSystem:
    def __init__(self):
          print("Welcome to Bank")
                    
    def withdraw(self, b:BankAccount, amount:float)-> str:
        if isinstance(b,Payroll) == True:
            if amount <= b.balance:
                b.balance-= amount
                return "You withdrawed a total of: " + str (amount) +  "\nYour New Balance is: " + str(b.balance)
            else:
                return "Error! Your Balance is"  + str(b.balance)
        elif isinstance(b,Debit) == True and isinstance(b,Debit) == True:
            if b.status == "Active":
                if amount <= b.balance:
                    b.balance-= amount
                    return "You withdrawed a total of: " + str (amount) +  "\nYour New Balance is: " + str(b.balance)
                else:
                    return "Error! Your Balance is"  + str(b.balance) 
            else:
                return "Your account is Inactive, Please Activate"
        elif isinstance(b,Credit) == True:
            if b.balance+amount < 1000000:
                b.balance+= amount
                return "You withdrawed a total of:" + str (amount) +  "\nYour New Credit Balance is:" + str(b.balance)
            else:
                return "Error! You Exceed your Credit limit"  

    def deposit(self,b:BankAccount, amount:int)-> str:   
        if isinstance(b,Payroll) == True:
            return "This is a PAYROLL Account you can't Deposit"
        elif isinstance(b,Debit) == True:
            if b.status == "Active":
                b.balance+= amount
                return "You Deposit a total of:" + str (amount) +  " Your New Balance is:" + str(b.balance)
            else:
                return "Your account is Inactive, Please Activate"
        elif isinstance(b,Credit) == True:
            if b.balance-amount > 0:
                b.balance-= amount
                return "You Deposit a total of:" + str (amount) +  " Your New Balance is:" + str(b.balance)
            else:
                return "Error! Please paid within this amount" + str(b.balance)
            
    def transfer (self,b1:BankAccount, b2:BankAccount, amount:int)-> str:
        if isinstance(b1,Payroll) == True:
            return "This is a PAYROLL Account you can't Transfer"
        elif isinstance(b1,Debit) == True:
            if b1.status == "Active":
                if isinstance(b2,Payroll) == True:
                    b1.balance -= amount
                    b2.balance += amount
                    return "Successfully Transferred"
                elif isinstance(b2,Debit) == True:
                    if b2.status == "Active":
                        b1.balance -= amount
                        b2.balance+= amount
                        return "Successfully Transferred"
                    else:
                        return "Error! The account is Inactive"
                elif isinstance(b2,Credit) == True:
                    if b2.balance-amount > 0:
                        b1.balance -= amount
                        b2.balance -= amount
                        return "Successfully Transferred"
                    else:
                        return "Error! Negative Balance account"
            else:
                return "Your account is Inactive, Please Activate"
        elif isinstance(b1,Credit) == True:
            if b1.balance+amount < 1000000:
                if isinstance(b2,Payroll) == True:
                        b1.balance += amount
                        b2.balance += amount
                        return "Successfully Transferred"
                elif isinstance(b2,Debit) == True:
                    if b2.status == "Active":
                        b1.balance += amount
                        b2.balance+= amount
                        return "Successfully Transferred"
                    else:
                        return "Error! The account is Inactive"
                elif isinstance(b2,Credit) == True:
                    if b2.balance-amount > 0:
                        b1.balance += amount
                        b2.balance -= amount
                        return "Successfully Transferred"
                    else:
                        return "Error! Negative Balance account"
            else:
                return "Error! You Exceed your Credit Limit"
            

    def Activation (self, b:BankAccount, choice: str, amount)->str:
        if isinstance(b,Payroll) == True:
            if choice == "Activate":
                b.status= "Inactive"
                return "You succesfully Activate your account"
            elif choice == "Deactivate":
                b.status= "Inactive"
                return "You succesfully deactivate your account"
        elif isinstance(b,Debit) == True:
            if choice == "Activate":
                if b.balance+amount>=100:
                    b.balance += amount
                    b.status= "Active"                    
                    return "You succesfully Activate your account"
                else:
                    return "Transaction Failed please deposit amount 100 pesos"
            elif choice == "Deactivate":
                b.status= "Inactive"
                return "You succesfully deactivate your account"
        elif isinstance(b,Credit) == True:
            if choice == "Activate":
                b.status= "Inactive"
                return "You succesfully Activate your account"
            elif choice == "Deactivate":
                b.status= "Inactive"
                return "You succesfully deactivate your account"

class AccountUpdate:
    def __init__(self, accountsList: {BankAccount}):
        self.__accountsList= accountsList
        print ("Monthly Accounts Updating")
    def monthlyUpdate(self):
        for accounts in self.__accountsList:
            if isinstance(accounts,Debit) == True:
                if accounts.balance<100:
                    accounts.status= "Inactive"                    
                else:
                    accounts.status= "Active"
                    accounts.balance = accounts.balance *(1+0.01)
            elif isinstance (accounts, Credit) ==True:
                accounts.balance = accounts.balance *(1+0.03)
            elif isinstance (accounts, Payroll) ==True:
                pass



### SAMPLE BANKING ###
        
p1:BankAccount = Payroll(1001, "Albedo", 4000.00, "Active")
p2:BankAccount = Payroll(1001, "Mona", 30000.00, "Active")
d1:BankAccount = Debit(1001, "Childe", 3000.00, "Active")
d2:BankAccount = Debit(1001, "Diluc", 50000.00, "Active")
c1:BankAccount = Credit(1001, "Eula", 0.00, "Active")
c2:BankAccount = Credit(1001, "Ganyu", 0.00, "Active")


### ACCOUNT INFORMATION

print(p1.accountInformation()+"\n")
print(p2.accountInformation()+"\n")
print(d1.accountInformation()+"\n")
print(d2.accountInformation()+"\n")
print(c1.accountInformation()+"\n")
print(c2.accountInformation()+"\n")

### Transaction 1
t1= BankingSystem()

### Withdrawal
print (t1.withdraw (p1, 3000)+"\n")
print (t1.withdraw (d1, 500)+"\n")
print (t1.withdraw (c1, 1000001)+"\n") ### error since it goes beyond the credit limit
print (t1.withdraw (c2, 10000)+"\n")

print(p1.balanceInformation()+"\n")
print(d1.balanceInformation()+"\n")
print(c1.balanceInformation()+"\n")
print(c2.balanceInformation()+"\n")

### Deposit
print (t1.deposit (p1, 3000)+"\n") ### error since it is a PAYROLL ACCOUNT
print (t1.deposit (d1, 50000)+"\n")
print (t1.deposit (c1, 1000)+"\n") ### error since it goes negative
print (t1.deposit (c2, 5000)+"\n") ###paying time

print(p1.balanceInformation()+"\n")
print(d1.balanceInformation()+"\n")
print(c1.balanceInformation()+"\n")
print(c2.balanceInformation()+"\n")

### Transfer
print (t1.transfer (p1, d1, 5000))
print (t1.transfer (d1, d2, 3000))
print(d1.balanceInformation()+"\n")
print(d2.balanceInformation()+"\n")
print (t1.transfer (c1, c2, 500))
print(c1.balanceInformation()+"\n")
print(c2.balanceInformation()+"\n")
print (t1.transfer (c2, d1, 500))
print(c2.balanceInformation()+"\n")
print(d1.balanceInformation()+"\n")

print(p1.balanceInformation()+"\n")

up1= AccountUpdate([p1,p2,d1,d2,c1,c2])
up1.monthlyUpdate()

print(p1.balanceInformation()+"\n")
print(p2.balanceInformation()+"\n")
print(d1.balanceInformation()+"\n")
print(d2.balanceInformation()+"\n")
print(c1.balanceInformation()+"\n")
print(c2.balanceInformation()+"\n")

