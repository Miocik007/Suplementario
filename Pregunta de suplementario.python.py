#Primero, genere un número aleatorio dentro de un rango, 
# por ejemplo, de 0 a 10. 
# Luego, solicite repetidamente a los usuarios que ingresen un número. 
# Si el número ingresado es más bajo o más alto que el número aleatorio, brinde una pista a los usuarios. 
# Si el número ingresado es igual al número aleatorio, el ciclo se detiene. 
# Nota: Si el valor del azar es mayor que el valor ingresado, mostrar "el valor debe ser mas grande" 
# Si el valor del azar es menor que el valor ingresado, mostrar "el valor debe ser mas pequeño" 
# En caso que el valor es igual al valor del rango, me muestra "Bingo".
import random
intento = 0
a = 1
b = 10
number = random.randint(0, 10)
print("Estoy pensando en un número del 0 al 10")
while intento < 10:
    print("Inserte un número")
    guess = input()
    guess = int(guess)
    intento = intento + 1
    if guess < number:
        print("Tu número es bajo")
    if guess > number:
        print("Tu número es alto")
    if guess == number:
        break
if guess == number:
    print("BINGO")#Primero, genere un número aleatorio dentro de un rango, 
