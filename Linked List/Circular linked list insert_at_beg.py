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

    def display(self):
        if self.start == None:
            print("List is empty")
            return

        temp = self.start

        while temp.next != self.start:
            print(temp.info, end=" -> ")
            temp = temp.next

        print(temp.info)


obj = circular_singly_list()

i = 1
while i <= 4:
    n = int(input("Enter item: "))
    obj.insert_at_beg(n)
    i += 1

obj.display()
