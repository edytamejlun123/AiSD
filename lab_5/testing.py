from binary_node import *

t1: BinaryTree = BinaryTree(3)
t1.root.right_child = BinaryTree(5)


assert t1.root.value == 3
assert t1.root.right_child.value == 5
