from __future__ import annotations
from typing import Any, List
from graphviz import *


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
        return f"{self.value}"

    def show(self, g=Digraph('g')):
        g.node(str(self), str(self), shape='circle')
        if self.left_child:
            g.edge(str(self), str(self.left_child), color='red')
            self.left_child.show()
        if self.right_child:
            g.edge(str(self), str(self.right_child), color='blue')
            self.right_child.show()
        return g


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
        self.root = self.__insert(self.root, value)

    def __insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node:
            if value < node.value:
                node.left_child = self.__insert(node.left_child, value)

            elif value == node.value:
                print(f"{node.value} -> ta wartość już jest w drzewie.")

            if value > node.value:
                node.right_child = self.__insert(node.right_child, value)

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

    def remove(self, value: Any) -> None:
        if self.contains(value):
            self.root = self.__remove(self.root, value)

    def __remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:

            if node.left_child and node.right_child:
                node.value = node.right_child.min().value
                node.right_child = self.__remove(node.right_child, node.right_child.min().value)

            elif node.left_child:
                node = node.left_child

            elif node.right_child:
                node = node.right_child

            else:
                node.value = 0

        elif value < node.value:
            node.left_child = self.__remove(node.left_child, value)

        else:
            node.right_child = self.__remove(node.right_child, value)

        return node

    def show(self) -> None:
        self.root.show().render(filename='bst', format='png', cleanup=True, view=False)
