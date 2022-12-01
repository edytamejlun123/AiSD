from binary_node import *

b1: BinaryNode = BinaryNode(3)
t1 = BinaryTree(b1)
t1.root.add_right_child(5)
t1.root.add_right_child(4)

assert t1.root.value == 3
assert t1.root.right_child.value == 5
b1.printTree()
