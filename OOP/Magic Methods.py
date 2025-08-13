class Bank:
    bank_name = "BOI"

    def __init__(self,name,balance,deposite):
        self.name=name
        self.balance = balance
        self.deposite = deposite

    def total_balance(self):
        return self.balance + self.deposite
    
obj=Bank("John", 1000, 500)

# 1] Dict returns all instance variables and their values in a dictionary format if u call it with object (instance variableonly)
print(obj.__dict__)    #instance variables
print(Bank.__dict__)  #class variables & methods
print(obj.bank_name) # accessing class variable using object

# 2] init automatically initialize the instant variables when an object is created
print(obj.name)
t=obj.total_balance()
print(t)


    

