# 

print("Introdueix 2 valors: ")
n1 = int(input())
n2 = int(input())

if n1 % 2 != 0:     # Si el primer nombre no és parell
    n1 += 1

suma = 0
producte = 1
nvalors = 0

for i in range (n1,n2+1,2): #Agafa valors entre l'1n i l'n2 cada 2 (parells)
    suma += i
    producte *= i
    nvalors += 1 

mitjana = suma / nvalors

print ("Suma:",suma,"- Producte:",producte,"- Mitjana: "+str(mitjana))
