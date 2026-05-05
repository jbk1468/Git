import random
import time

punktyU = 0
punktyK = 0


while True:
    wybor = input("Orzel(o) czy reszka(r)? ")
    
    if wybor ==  "o" or wybor == "r":

        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)


        rzut = random.choice(["orzeł", "reszka"])
        print(rzut)

        if wybor == "o":
            if rzut == "orzeł":
                print("Zwyciestwo")
                punktyU = punktyU + 1
                print(punktyU, punktyK)
            else:
                print("Przegrana")
                punktyK = punktyK + 1
                print(punktyU, punktyK)
        elif wybor == "r":
            if rzut == "reszka":
                print("Zwyciestwo")
                punktyU = punktyU + 1
                print(punktyU, punktyK)
            else:
                print("Przegrana")
                punktyK = punktyK + 1
                print(punktyU, punktyK)
    elif wybor == "0":
        break
    else:
        print("Wybierz o lub r")