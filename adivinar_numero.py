
import random

numero_secreto = random.randint(1,100)
adivinado = False
intentos = 0
limite_intentos = 5

print('Bienvenido al juego de la adivinanza.')

while not adivinado and intentos < limite_intentos:

    numero = int(input('Ingrese un número: '))
    intentos += 1
    if numero == numero_secreto:
        print('Felicitaciones, adivinó el número en ' + str(intentos) +' intentos.')
        adivinado = True
    elif numero < numero_secreto:
        print('El número secreto es mayor al ingresado')
    elif numero > numero_secreto:
        print('El número secreto es menor al ingresado')

if limite_intentos == intentos and not adivinado:
    print('Game Over, llegó al límite de intentos ' + str(limite_intentos))
        




