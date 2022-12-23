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

    assert r1.contains(8) == True

    drzewo = BinarySearchTree(BinaryNode(8))
    drzewo.insert(3)
    lista = (5, 6, 8, 2, -2, 17)
    drzewo.insert_list(lista)

    drzewo.show()

    assert drzewo.contains(6) == True


if __name__ == "__main__":
    main()
