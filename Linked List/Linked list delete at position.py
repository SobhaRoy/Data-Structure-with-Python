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
    def delete_at_beg(self):
        if(self.start==None):
            print("List is empty")
        elif(self.start.next==None):
            start=None
        else:
            temp=self.start
            self.start=temp.next
            del temp
    def delete_at_position(self,pos):
        if(pos==1):
            delete_at_beg()
        else:
            i=1
            temp=self.start
            while(temp.next!=None and i<pos):
                prev=temp
                temp=temp.next
                i+=1
            if(temp.next==None):
                print("deletion is not possible")
                return
            else:
                print("Deleted item is:",temp.info)
                prev.next=temp.next
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
position=int(input("Enter the position:"))
obj1.delete_at_position(position)

print("After deletion list is:")
obj1.display()

