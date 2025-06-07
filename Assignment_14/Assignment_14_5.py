class BankAccount:
    school_name = "ABC International School"
   
    def __init__(self, accNo, name, balance):
        self.Account_Number = accNo
        self.Name = name
        self.Balance = balance

    def Deposit(self, amt):
        self.Balance += amt
        print(amt, " deposited successfully")
        
    def Withdraw(self, amt):
        if(self.Balance < amt):
            print("Insufficient Balance, Withdrawal Cancelled!!")
            return
        self.Balance -= amt
        print(amt, "withdrawn succesfully")
        
    def DisplayBalance(self):
        print("Available Balance: ", self.Balance)

def main():
    obj = BankAccount(8761216, 'Suraj', 5000)
    obj.DisplayBalance()
    obj.Deposit(1000)
    obj.DisplayBalance()
    obj.Withdraw(500)
    obj.DisplayBalance()
    obj.Withdraw(5501)
    obj.DisplayBalance()


if __name__ == "__main__":
    main()