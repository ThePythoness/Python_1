# OrdenarLlista

from llistes import LlegirLlista 

MIDA = 8

def OrdenarLlista(llista):
    for i in range (1,len(llista)):
        for j in range (0,len(llista) - i):
            if llista[j] > llista[j+1]:
                llista[j], llista[j+1] = llista[j+1],llista[j]

#Programa principial
L = LlegirLlista(MIDA)
print(L)
OrdenarLlista(L)
#ordenarlista

