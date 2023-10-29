
# Any de traspàs

anyt = int(input("Introdueix un any de traspàs: "))


if (anyt % 4 == 0 and anyt % 100 != 0) or anyt % 400 == 0:    # La "!" significa que NO compleix, No és estrictament igual 
    print("A l'any",anyt,"febrer té 29 dies")
else:
    print("A l'any",anyt,"febrer té 28 dies")











    


