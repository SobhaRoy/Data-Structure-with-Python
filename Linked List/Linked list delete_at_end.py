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
    def delete_at_end(self):
        if(self.start==None):
            print("List is empty")
        elif(self.start.next==None):
            start=None
        else:
            temp=self.start
            while(temp.next!=None):
                prev=temp
                temp=temp.next
            prev.next=None
            del temp
                
            
        
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
print("Before deletion the list is:")
obj1.display()
obj1.delete_at_end()
print("After deletion list is:")
obj1.display()

