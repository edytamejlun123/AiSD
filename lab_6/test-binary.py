from binarynode import *


def main() -> None:
    n1 = BinaryNode(8)
    n2 = BinaryNode(3)
    # n3 = BinaryNode(1)
    # n4 = BinaryNode(10)

    # n1.left_child = n2
    # n1.right_child = n4
    # n2.left_child = n3
    #
    # assert n1.min() == n3

    r1 = BinarySearchTree(n1)
    r2 = BinarySearchTree(n2)
    r1.root.left_child = r2
    # r1._insert(n1, 2)
    # assert r1.root.min() ==
    assert r1.contains(8) == True
    assert r1.contains(3) == True


if __name__ == "__main__":
    main()
