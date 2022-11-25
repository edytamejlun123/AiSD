from typing import Any, Callable
from graphviz import *

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value

    def is_leaf(self) -> bool:
        if self.right_child == None or self.left_child == None:
            return True
        return False

    def add_left_child(self, value: Any) -> None:
        self.left_child = value

    def add_right_child(self, value: Any) -> None:
        self.right_child = value

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)


    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.traverse_post_order(visit)
        if self.right_child:
            self.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.traverse_pre_order(visit)

    def printTree(self) -> None:
        print(self.value)

    def show(self, graf = Graph('g')):
        graf.node(str(self), str(self.value), shape="circle")



class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)
