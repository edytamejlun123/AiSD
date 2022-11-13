nazwy_dni = {1: 'poniedzialek', 2: 'wtorek', 3: 'sroda',
             4: 'czwartek', 5: 'piatek', 6: 'sobota',
             7: 'niedziela'}
def ktory_dzien(n: int):
    return nazwy_dni[n]
print(ktory_dzien(3))
print(ktory_dzien(1))
print(ktory_dzien(6))