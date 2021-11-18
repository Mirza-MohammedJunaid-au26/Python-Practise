class Node():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
dic = {}
k = 1
l = []
tree_inp = int(input("How Many Nodes You Want :"))

for i in range(tree_inp):
    node_data = int(input("Enter Data :"))
    dic[k] = Node(node_data)
    k += 1

def link():
    pass
