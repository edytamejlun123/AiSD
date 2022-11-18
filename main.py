from zadanie import *

def main():
    drzewo1 = TreeNode('F')
    drzewo1.add(TreeNode('B'))
    drzewo1.add(TreeNode('G'))
    drzewo1.children[0].add(TreeNode('A'))
    drzewo1.children[0].add(TreeNode('D'))

    poddrzewo = Tree(drzewo1)
    poddrzewo.add('C', poddrzewo.root.children[0].children[1])

    # print(poddrzewo.root.is_leaf())

    # poddrzewo.for_each_deep_first(print_node)
    # print('~')
    # poddrzewo.for_each_level_order(print_node)
    # poddrzewo.for_each_deep_first(print_node)
    # poddrzewo.printer()



    kat = TreeNode('kategorie')
    kat.add(TreeNode('colors'))
    kat.add(TreeNode("Animals"))
    kat.children[0].add(TreeNode("Red"))
    kat.children[0].add(TreeNode("Pink"))
    kat.children[0].add(TreeNode("Black"))

    kat2 = Tree(kat)
    kat2.add('Cat', kat2.root.search("Animals"))

    kat2.for_each_level_order(print_node)
    kat2.printer()

    print("\n$$$$$\n")

    a1 = TreeNode(5)
    a2 = TreeNode(3)
    a3 = TreeNode(1)
    a4 = TreeNode(8)
    a1.add(a2)
    a2.add(a3)
    a1.add(a4)

    a1.for_each_deep_first(print_node)
    print('\nxxxxx\n')
    a1.for_each_level_order(print_node)


if __name__ == '__main__':
    main()
