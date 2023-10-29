 
# Positiu, negatiu o zero

num = int(input("Introdueix un nombre: "))

if (num > 0):
    sortida = "Positiu"
else:
    if (num < 0):
        sortida = "Negatiu"
    else:
        sortida = "Zero"

print(sortida)