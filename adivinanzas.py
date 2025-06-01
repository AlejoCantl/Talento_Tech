from random import randint

def adivinanza(numero):
    intentos = 0
    numero_secreto = randint(1, numero)
    print(f"Estoy pensando en un número entre 1 y {numero}. ¡Adivina cuál es!")
    while True:
        try:
            adivinanza_usuario = int(input("Introduce el numero que crees que es: "))
            intentos+=1

            if adivinanza_usuario > numero or adivinanza_usuario < 1:
                print(f"El número debe estar entre 1 y {numero}. Inténtalo de nuevo.")
            elif adivinanza_usuario < numero_secreto:
                print("Demasiado bajo. Inténtalo de nuevo.")
            elif adivinanza_usuario > numero_secreto:
                print("Demasiado alto. Inténtalo de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

print("Bienvenido al juego de adivinanza de números.")

rango = input("¿Cuál es el rango máximo para el número secreto? (por defecto 100): ")

if rango.isdigit() or rango == "":
    if rango == "":
        rango = 100
    else:
        rango = int(rango)

adivinanza(rango)