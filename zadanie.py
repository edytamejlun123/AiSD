from typing import List, Any, Callable, Union
from graphviz import *

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, v: Any) -> None:
        self.value = v
        self.children = []


    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def is_leaf(self) -> bool:
        if self.children == None:
            return True
        return False

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        fifo = []
        fifo.append(self)
        while fifo:
            visit(fifo[0])
            for e in fifo[0].children:
                fifo.append(e)
            fifo.pop(0)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for e in self.children:
            e.for_each_deep_first(visit)

    def search(self, v: Any) -> Union['TreeNode', None]:
        if self.value == v:
            return self
        for e in self.children:
            if e.search(v):
                return e.search(v)
        return None

    def show(self, graf=Graph('g')):
        graf.node(str(self), str(self.value), shape='doublecircle')
        for e in self.children:
            graf.edge(str(self), str(e))
            e.show(graf)
        return graf



class Tree:
    root: TreeNode

    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def printer(self) -> None:
        self.root.show().render(format='jpg', filename='Treesy', view=True,
                                      cleanup=True)



def print_node(tree: 'TreeNode') -> None:
    if isinstance(tree, TreeNode):
        print(tree.value)
    else:
        print(tree)

