# Importar la biblioteca Random

import random

 

# Cargar en una variable un numero aleatorio
numero = random.randint(1,100)
adivinado = 0
print(numero)

print("Bienvenidos al juego de adivinar el numero que estoy pensando")

while adivinado == 0:
    num = input("ingresar un numero para adivinar el que estoy pensando: ")
    entrada = int(num)

    if entrada == numero:
        print("Felicidades, adivinaste el numero secreto")
        adivinado = 1
    elif numero < entrada:
        print("El numero secreto es menor")
    else:
        print("El numero secreto es mayor")
