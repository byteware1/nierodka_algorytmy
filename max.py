lista = [4,2,4,5,6,7,121,5,3,1,3]

m = lista[0]           # przyjmujemy pierwszy element jako największy
for x in lista[1:]:    # przechodzimy po reszcie elementów
    if x > m:           # jeśli coś jest większe
        m = x           # aktualizujemy największą wartość

print(m)               # wypisujemy wynik