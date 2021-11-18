class Node:

    def __init__(self,data):
        self.Data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root == None:
        return
    
    inOrder(root.left)
    print(root.Data)
    inOrder(root.right)


def insert(root,data):

    if root == None:
        return Node(data)

    if data > root.Data:
        root.right = insert(root.right,data) 
    elif data < root.Data:
        root.left = insert(root.left,data) 

    return root

root = None

root = insert(root,1)
root = insert(root,2)
root = insert(root,3)
inOrder(root)