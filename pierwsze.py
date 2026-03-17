n = 7          # liczba, którą sprawdzamy
i = 2          # zaczynamy od 2, bo 1 dzieli każdą liczbę

while i < n:   # sprawdzamy wszystkie liczby od 2 do n-1
    if n % i == 0:          # jeśli n dzieli się przez i bez reszty
        print("to nie jest liczba pierwsza")  # znaleziono dzielnik → nie pierwsza
        break               # kończymy pętlę, bo już wiemy
    i += 1                  # zwiększamy i i sprawdzamy następny dzielnik
else:
    # else wykona się tylko jeśli while zakończy się normalnie (bez break)
    print("to jest liczba pierwsza")  # nie znaleziono żadnego dzielnika → liczba pierwsza