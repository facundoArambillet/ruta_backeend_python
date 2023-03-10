from node import Node

node_2 = Node("A",None)
node_3 = Node("B",node_2)
node_1 = Node("C",node_3)

print(node_3.next.data)
print(node_1.next.data)
 