from __future__ import annotations
from typing import Any, List


class BinaryNode:
    value: Any
    left_child: BinaryNode
    right_child: BinaryNode

    def __init__(self, value: Any = None) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> BinaryNode:
        counter = self

        while counter.left_child is not None:
            counter = counter.left_child

        return counter


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root

    # def _insert(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':
    #     self.root = node
    #     if value < self.root.value:
    #         self.root.left_child = self._insert(self.root.left_child, value)
    #
    #     if value >= self.root.value:
    #         self.root.right_child = self._insert(self.root.right_child, value)
    #
    #     return BinaryNode(value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            if node.left_child is None:
                node.left_child = BinaryNode(value)
            self._insert(node.left_child, value)

        if value >= node.value:
            self._insert(node.right_child, value)

        return BinaryNode(value)

    def insert(self, value: Any) -> None:
        a: BinaryNode = BinaryNode(value)
        self._insert(a, value)
        self.root = a

    def insert_list(self, lista: List[Any]) -> None:
        for i in lista:
            self.insert(i)

    def contains(self, value: Any) -> bool:

        if value < self.root.value:
            self.root = self.root.left_child
            self.contains(value)

        elif value > self.root.value:
            self.root = self.root.right_child
            self.contains(value)

        elif value == self.root.value:
            return True

        else:
            return False

    # def _remove(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':
    #     if self.root.left_child is None and self.root.right_child is None:
    #         self.root = node
    #         del node
    #     if self.root.value > value:

    def __str__(self) -> str:
        wynik = ''
        if self.root:
            if self.root.value:
                wynik += (str(self.root.value) + '->')
