class queue:
    def __init__(self):
        self.size=int(input("Enter the size of the queue:"))
        self.l=[0]*self.size
        self.front=-1
        self.rear=-1
    def insertion(self):
        if self.front==self.size-1:
            print("queue overflow")
        item=int(input("Enter a item:"))
        self.front=self.front+1
        self.l[self.front]=item
        if(self.rear==-1):
            self.rear=0
        
    def deletion(self):
        if self.rear==-1:
            print("queue is empty")
        if(self.front==self.rear):
            self.front=-1
            self.rear=-1
        item=self.l[self.rear]
        print("delete item is:",item)
        self.rear=self.rear+1
        
    def display(self):
        for i in range(self.rear,self.front+1):
            print(self.l[i])
obj=queue()
while(True):
    print("Enter 1 for insertion or 2 for deletion or 3 for display or 0 for exit:");
    n=int(input("Enter your choice:"))
    if(n==1):
        obj.insertion()
    elif(n==2):
        obj.deletion()
    elif(n==3):
        obj.display()
    elif(n==0):
        break
    else:print("wrong input")

