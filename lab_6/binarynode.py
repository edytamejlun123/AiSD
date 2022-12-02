from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value

    def min(self) -> 'BinaryNode':
        counter = self

        while counter.left_child is not None:
            counter = counter.left_child

        return counter

    def insert(self, value: Any) -> BinaryNode:
        if self.value > value:
            self.left_child =

class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root

    def insert(self, value: Any) -> None:
