class Node:
    def __init__(self,item):
        self.info=item
        self.right=None
        self.left=None
class binary_search_tree:
    def __init__(self):
        self.root=None
    def insert(self,item):
        nd=Node(item)
        if(self.root==None):
            self.root=nd
            return
        temp=self.root
        while(temp!=None):
            if(item>temp.info):
                parent=temp
                temp=temp.right
            else:
                parent=temp
                temp=temp.left
        if(parent.info<item):
            parent.right=nd
        else:
            parent.left=nd

def inorder(nd):
    if(nd!=None):
        inorder(nd.left)
        print(nd.info)
        inorder(nd.right)
        
bst = binary_search_tree()
bst.insert(65)
bst.insert(32)
bst.insert(10)
bst.insert(6)
bst.insert(64)
inorder(bst.root)



        
