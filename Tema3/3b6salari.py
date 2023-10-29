
#  Càlcul salari

sbase = float(input("Introdueix el teu salari base: "))
antig = int(input("Introdueix la teva antiguitat: "))

if (antig < 3):
    final = sbase*1.01
else:
    if (antig < 5):
        final = sbase*1.02
    else:
        final = sbase*1.035

print("El salari final és: " +str(final))