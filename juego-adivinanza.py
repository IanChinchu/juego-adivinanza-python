

import random


numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Adivinemos el numero secreto")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Elegi numero del 1 al 99: ")
    numero = int(entrada)
    
    if numero == numero_secreto:
        print("Adivinaste pa")
        adivinado = True
    elif numero < numero_secreto:
        print("cerca, el numero es mayor al que pusiste")
    else:
        print("el numero es menor al que pusiste")
    cant_intentos +=1
if  not cant_intentos < cant_max_intentos:
    print("Game Over. Fallaste 5 intentos")   



