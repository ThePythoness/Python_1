
# Ordenar 2 nombres de menor a major

num1 = int(input("Introdueix un primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))


if num1 > num2:          
    num1,num2 = num2,num1

#Alternativa llarga:
# aux = num2
# num2 = num1
# num1 = aux

print ("El valor de num1 és",num1,"i el valor de num2 és",num2)