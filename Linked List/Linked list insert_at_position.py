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
    def insert_at_position(self,item,pos):
        nd=node(item)
        if(pos==1):
            self.insert_at_begi(item)
        else:
            i=1
            temp=self.start
            while(temp.next!=None and i<pos):
                prev=temp
                temp=temp.next
                i=i+1
            if(temp.next==None):
                temp.next=nd
                return
            nd.next=temp
            prev.next=nd
        
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
item=int(input("Enter the item:"))
position=int(input("Enter the position:"))
obj1.insert_at_position(item,position)
obj1.display()
