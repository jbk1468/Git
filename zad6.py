def AlgBinarny(lista, szukana):
    lewy = 0
    prawy = len(lista) - 1

    while lewy <= prawy:
        srodek = int((lewy + prawy) / 2)

        if lista[srodek] == szukana:
            return srodek

        if lista[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return -1


numbers = [3, 1, 4, 5, 9, 7, 14]
lista = sorted(numbers)
szukana = 9

wynik = AlgBinarny(lista, szukana)
print("szukana: ", szukana)
print("indeks: ", wynik)