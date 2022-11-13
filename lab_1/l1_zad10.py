def palindrom(lista):
    koniec = len(lista)-1
    for i in range(0, len(lista)):
        if(lista[i] != lista[koniec-i]):
            return 0
    return 1
lista = [1,2,3,2,1]
print(palindrom(lista))