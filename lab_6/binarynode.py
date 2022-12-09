from typing import Any, List


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


class BinarySearchTree:
    root: 'BinaryNode'

    def __init__(self, root: 'BinaryNode') -> None:
        self.root = root

    def _insert(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':
        self.root = node
        if value < self.root.value:
            self.root.left_child = self._insert(self.root.left_child, value)

        if value >= self.root.value:
            self.root.right_child = self._insert(self.root.right_child, value)

        return BinaryNode(value)

    def insert(self, value: Any) -> None:
        self._insert(self.root, value)

    def insert_list(self, lista: List[Any]) -> None:
        for i in lista:
            self.insert(i)

    def contains(self, value: Any) -> bool:

        if value < self.root.value:
            self.root = self.root.left_child
            self.contains(value)

        if value > self.root.value:
            self.root = self.root.right_child
            self.contains(value)

        if value == self.root.value:
            return True

        return False

    def _remove(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':
        if self.root.left_child is None and self.root.right_child is None:
            self.root = node
            del node
        if node.value > value:
