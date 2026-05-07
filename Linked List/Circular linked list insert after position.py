class node:
    def __init__(self,item):
        self.info=item
        self.next=None
class circular_singly_list:
    def __init__(self):
        self.start=None
    def insert_at_last(self,item):
        nd=node(item)
        if(self.start==None):
            self.start=nd
            self.start.next=self.start
            return
        temp=self.start
        while(temp.next!=self.start):
            temp=temp.next
            
        temp.next=nd
        nd.next=self.start


    def insert_after_position(self,item,loc):
        nd=node(item)
        i=1
        temp=self.start
        while(i<loc and temp.next!=self.start):
            prev=temp
            temp=temp.next
            i+=1
        if(temp.next!=self.start):
            nd.next=temp
            prev.next=nd
        else:
            nd.next=temp.next
            temp.next=nd
    def display(self):
        ptr = self.start
        while ptr.next != self.start:
            print(ptr.info, end=" -> ")
            ptr = ptr.next

        print(ptr.info)

obj1=circular_singly_list()
i=1
while(i<=4):           
    n=int(input("Enter item:"))
    obj1.insert_at_last(n)
    i+=1
item=int(input("Enter the item:"))
position=int(input("Enter the position:"))
obj1.insert_after_position(item,position)
obj1.display()
