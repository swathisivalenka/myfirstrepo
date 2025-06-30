class Bank:
    def __init__(self):
        self.__balance = 0 # 2 underscores __varname is a private variable 
    def deposit(self,amount):
        self.__balance+= amount
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount>self.__balance or amount<0:
            print("Insufficient Balance")
        else:
            self.__balance-=amount
    
b = Bank()
b.deposit(2000)
#print(b.__balance)
#print(b.get_balance())
b.withdraw(5000)
b.withdraw(-100)
print(b.get_balance())


        