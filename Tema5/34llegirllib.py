# Guardar en estructura de dades temperatura

from llistes import LlegirLlista, InicialtizarLLista, MaximLlista, MinimLlistaNoZero

N_DIES = 14 
N_TEMP = 61    #De -10 a 50 graus
print("Introdueix les temperatures: ")
temp = LlegirLlista(N_DIES)

histo = InicialtizarLLista(N_TEMP,0)   #Inicialitzem la llista a 0

for i in range(len(temp)):
    ind_histo = temp[i]+10 #Index histograma on hem de sumar 1
    histo[ind_histo] += 1  
print(histo)     

print("Temperatura més repetida: ",MaximLlista(histo)-10)
print("Temperatura menys repetida: ", MinimLlistaNoZero(histo)-10)
#restem 10 a l'index del màxim i del mínim per saber a quina temperatura correspon




