lista = [4,4,5,5,3,3]   # lista liczb
suma = 0                 # zmienna do sumy
i = 0                    

while i < len(lista):    # przechodzimy przez wszystkie elementy listy
    suma += lista[i]     # dodajemy element do sumy
    i += 1               # idziemy do następnego elementu

print(suma / len(lista)) # średnia = suma / ilość elementów