# Comptar positius i negatius

npos = 0
nneg = 0
i = 0

for i in range (1,6):
    entrada = int(input("Introdueix un valor: "))
    if entrada > 0:
        (npos) += 1
    elif entrada < 0:
        nneg += 1
    i += 1

print("Positius: "+str(npos)+" - Negatius: "+str(nneg))
