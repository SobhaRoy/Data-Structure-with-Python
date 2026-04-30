class node:
    def __init__(self,item):
        self.info=item
        self.next=None
class singlylist:
    def __init__(self):
        self.start=None
    def insert_at_begi(self,item):
        nd=node(item)
        nd.next=self.start
        self.start=nd
        
    def display(self):
        temp=self.start
        while(temp!=None):
            print(temp.info)

            temp=temp.next

obj1=singlylist()
i=1
while(i<=4):           
    n=int(input("Enter item:"))
    obj1.insert_at_begi(n)
    i+=1
obj1.display()
