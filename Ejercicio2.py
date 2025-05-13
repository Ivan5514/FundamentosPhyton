########################################################
# Calcular el preimetro y area de un rectangulo dada su base y su altura
########################################################

print("Programa que calcula area y perimetro")

altura = input("Ingresa la altura ")
altura = int(altura)
base =int(input ("ingresa la base: "))

perimetro = base + altura + base + altura
area= base * altura 

print("El area del rectangulo es: " + str(area))
print("El perimetro del rectangulo es: " + str(perimetro))