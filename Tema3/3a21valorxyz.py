
# Espressions lògiques

x = int(input("Introdueix un nombre x: "))
y = int(input("Introdueix un nombre y: "))
z = int(input("Introdueix un nombre z: "))

res1 = (x<7) and ((y>z) or (7>z))
res2 = ((x == 99) and (y < -5)) and ((z >= 100) or (z < 6))
res3 = ((9 >= x) and (13<y)) or (-36>=z)

print("Resultat de les expressions: "+str(res1)+", "+str(res2)+", "+str(res3))

