L = 9

def sumowanie(tab):
    
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i] + tab[j] == L:
                print(tab[i])
                print(tab[j])
                break
            
A = [1,3,5,2,11,7]
sumowanie(A)