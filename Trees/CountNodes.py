count = 0
def inOrder(root):
    global count
    if root == None:
        return
    inOrder(root.left)
    print(root.data)
    count += 1
    inOrder(root.right)
    return count

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)
Node8 = Node(8)
Node9 = Node(9)

root = None
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5
Node3.left = Node6
Node3.right = Node7
Node4.left = Node8
Node4.right = Node9
root = Node1
print("count :",inOrder(root))

