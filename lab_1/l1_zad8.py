def krotka(n):
    tab = []
    for i in range(0,n):
        b = input()
        tab.append(b)
    a = tuple(tab)
    return a
print(krotka(3))