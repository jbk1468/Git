def bubble(tab):
    for i in range(len(tab)):
        for j in range(0, len(tab)-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab
A = [2,1,5,3,6]
print(A)
print("Sortowanie bąbelkowe:")
print(bubble(A))