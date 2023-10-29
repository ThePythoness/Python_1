# Llibreria matemàtiques d'operacions genèriques

def LlegirLlista(nelements):      #Definim la funció i posem els nelements
    llista = []
    for i in range(nelements):
            llista.append(int(input("Introdueix el valor de la posició "+str(i)+": ")))
    return llista
    
def InicialtizarLLista(nelements, valor):
    llista = []
    for i in range(nelements):
         llista.append(valor)
    return llista

def MitjanaLlista(llista):
    suma = 0 
    for i in range(len(llista)):
        suma += llista[i]
    mitjana = suma / len(llista)
    return mitjana

def MaximLlista(llista):
    v_max = llista[0]
    pos_max = 0
    for i in range(len(llista)):
        if llista[i] > v_max:
            val_max= llista[i]
            pos_max = i
    return pos_max
     
def MinimLlista(llista):
    v_min = llista[0]
    pos_min = 0
    for i in range(len(llista)):
        if llista[i] < v_min:
            val_min = llista[i]
            pos_min = i
    return pos_min

def MinimLlistaNoZero(llista):
    index_1er_nozero = 0
    while index_1er_nozero < len(llista) and llista[index_1er_nozero] == 0:
        index_1er_nozero += 1
    if index_1er_nozero < len(llista):
        val_min = llista[index_1er_nozero]
        pos_min = index_1er_nozero
        for i in range(index_1er_nozero, len(llista)):
            if llista[i] != 0 and llista[i] < val_min:
                val_min = llista[i]
                pos_min = i
    else:          #La llista només conté zeros , retorna -1 pedr indicar el error
        val_min = -1
        pos_min = -1
    return pos_min