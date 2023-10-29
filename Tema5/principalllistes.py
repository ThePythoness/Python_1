# Programa pinrcipar pel provar llistes.py

from llistes import InicialtizarLLista, LlegirLlista, MaximLlista, MinimLlista, MinimLlistaNoZero, MitjanaLlista

MIDA = 6

L = InicialtizarLLista(MIDA,0)
print(L)

L = LlegirLlista(MIDA)
print(L)

print("Mitjana",MitjanaLlista(L))
print("Maxim",MaximLlista(L))
print("Minim",MinimLlista(L))
print("Posicio no zero",MinimLlistaNoZero(L))
