s = "Ala ma kota"

def liczSlowa(tekst):
    slowa = tekst.split()
    liczbaSlow = 0

    for i in slowa:
        liczbaSlow += 1

    return liczbaSlow


def liczLitery(tekst):
    litery = tekst.replace(" ", "")
    liczbaLiter = 0

    for i in litery:
        liczbaLiter += 1

    return liczbaLiter

def czestotliwosc(tekst):
    czetsotliwosci = []
    ablabet = [["a", 0], ["b", 0], ["c", 0], ["d", 0], ["e", 0], ["f", 0], ["g", 0], ["h", 0], ["i", 0], ["j", 0], ["k", 0], ["l", 0], ["m", 0], ["n", 0], ["o", 0], ["p", 0], ["q", 0], ["r", 0], ["s", 0], ["t", 0], ["u", 0], ["v", 0], ["w", 0], ["x", 0], ["y", 0], ["z", 0]]
    litery = tekst.replace(" ", "")
    for i in litery:
        for j in ablabet:
            if i.lower() == j[0]:
                j[1] += 1
                
    for z in ablabet:
        if(z[1] > 0):
            czetsotliwosci.append(z)
    return czetsotliwosci


print(s)
print("Slowa: ", liczSlowa(s))
print("Litery: ", liczLitery(s))
print(czestotliwosc(s))