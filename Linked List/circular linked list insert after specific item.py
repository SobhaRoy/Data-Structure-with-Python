class node:
    def __init__(self, item):
        self.info = item
        self.next = None


class circular_singly_list:
    def __init__(self):
        self.start = None

    def insert_at_beg(self, item):
        nd = node(item)

        
        if self.start == None:
            self.start = nd
            nd.next = self.start
            return

        
        temp = self.start
        while temp.next != self.start:
            temp = temp.next

        
        nd.next = self.start
        temp.next = nd
        self.start = nd

    def insert_after_specific_item(self,item,specific_item):
        nd = node(item)
        temp=self.start
        while(temp.info!=specific_item and temp.next!=self.start):
            temp=temp.next
        nd.next=temp.next
        temp.next=nd

    def display(self):

        ptr = self.start

        while ptr.next != self.start:
            print(ptr.info, end=" -> ")
            ptr = ptr.next

        print(ptr.info)


obj = circular_singly_list()

i = 1
while i <= 4:
    n = int(input("Enter item: "))
    obj.insert_at_beg(n)
    i += 1
item=int(input("Enter the item:"))
specific_item=int(input("Enter specific item:"))
obj.insert_after_specific_item(item,specific_item)

obj.display()
