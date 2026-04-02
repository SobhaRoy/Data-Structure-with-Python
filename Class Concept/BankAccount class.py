class BankAccount:
    def __init__(self,p,depo_am,with_am):
        self.p=p
        self.depo_am=depo_am
        self.with_am=with_am
    def deposit(self):
        self.new_depo=self.p+self.depo_am
        print("Before deposit the amount is:",self.p)
        print("After deposit the value is:",self.new_depo)
    def withdraw(self):
        if self.new_depo>=self.depo_am:
            self.new_with=self.new_depo - self.with_am
            print("Before withdraw the amount is:",self.p)
            print("After withdraw the value is:",self.new_with)
S1=BankAccount(1000,50,50)
S1.deposit()
S1.withdraw()
    
    
