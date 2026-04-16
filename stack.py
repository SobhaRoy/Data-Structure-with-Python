class stack:
    def __init__(self):
        self.l=[0]*3
        self.top=-1
    def push(self):
        if self.top==2:
            print("stack overflow")
            return
        item=int(input("Enter a item:"))
        self.top=self.top+1
        self.l[self.top]=item
        
    def pop(self):
        if self.top==-1:
            print("stack underflow")
            return
        item=self.l[self.top]
        print("pop item is:",item)
        self.top=self.top-1
        
    def display(self):
        for i in range(0,self.top+1):
            print(self.l[i])
obj=stack()
while(True):
    print("Enter 1 for push or 2 for pop or 3 for display or 0 for exit:");
    n=int(input("Enter your choice:"))
    if(n==1):
        obj.push()
    elif(n==2):
        obj.pop()
    elif(n==3):
        obj.display()
    elif(n==0):
        break
    else:print("wrong input")

