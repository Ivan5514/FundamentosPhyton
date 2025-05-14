##############################################################################################
#Dados los catetos de un triangulo rectangulo calcular su hipótenusa
#################################################################################################

# hipotenusa ** 2 = cateto1 ** 2 + cateto2 ** 2
##El operador doble asterisco ** permite elevar un numero 
## a una potencia n 

##para peraciones matematicas avanzadas logaritmicas
## la libreria math
import math

cateto1 = int(input('ingresa el valor del cateto1:  '))
cateto2 = int(input('ingresa el valor del cateto2:  '))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print('la hipotenusa del triangulo es: ' + str(hipotenusa))
