dic = {}
lvl = 1
def LeftView(root):
    
    global lvl

    if root == None:
        return

    if lvl not in dic:
        print(root.data)
        dic[lvl] = 1
    
    lvl += 1
    LeftView(root.left)
    LeftView(root.right)
    lvl -= 1


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
Node10 = Node(10)

root = None
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node4.right = Node5
Node3.left = Node7
Node7.left = Node9
Node9.right = Node10

root = Node1
LeftView(root)


# Output : 1,2,4,5,10

"""
               1
        2               3
    4               7
        5       9
                    10   

"""