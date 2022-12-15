from __future__ import annotations
from typing import Any, List


class BinaryNode:
    value: Any
    left_child: BinaryNode
    right_child: BinaryNode

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> BinaryNode:
        counter = self

        while counter.left_child is not None:
            counter = counter.left_child

        return counter

    def __str__(self) -> str:
        return f"{self.value}, \nlewe dziecko: {self.left_child}," \
               f"prawe dziecko{self.right_child}"


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
    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node:
            if value < node.value:
                node.left_child = self._insert(node.left_child, value)

            if value >= node.value:
                node.right_child = self._insert(node.right_child, value)
        else:
            node = BinaryNode(value)
        return node



    def insert_list(self, lista: List[Any]) -> None:
        for i in lista:
            self.insert(i)

    def contains(self, value: Any) -> bool:
        counter = self.root
        while counter:
            if value < counter.value:
                counter = counter.left_child

            if value > counter.value:
                counter = counter.right_child

            if value == counter.value:
                return True

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
