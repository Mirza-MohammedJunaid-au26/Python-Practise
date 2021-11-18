class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node2

head = Node1
temp = head
i = temp.next
j = temp.next.next
while temp!= None:
    if i != j:
        print(temp.data,end="-> ")
        temp = temp.next
        i = i.next
        j = j.next.next
    elif i==j:
        print("Cycle is present")
        break

print()