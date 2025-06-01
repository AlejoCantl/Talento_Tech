numero_1 = int(input("ingrese el primer numero: "))
numero_2 = int(input("ingrese el segundo numero: "))

operacion = input("""Ingrese el numero de la operacion que desea realizar: \n
1. Sumar
2. Restar
3. Multiplicar
4. Dividir

""")

switcher = {
    "1": numero_1 + numero_2,
    "2": numero_1 - numero_2,
    "3": numero_1 * numero_2,
    "4": numero_1 / numero_2 if numero_2 != 0 else "Incapaz de dividir por cero"
}

operacionMessage = {
    "1": "suma",
    "2": "resta",
    "3": "multiplicación",
    "4": "división"
}


resultado = switcher.get(operacion, "Operación no válida")
print("""\n""")
if resultado != "Operación no válida":
    if resultado != "Incapaz de dividir por cero":
        print(f"El resultado de la {operacionMessage.get(operacion)} es: {resultado}")
    else:
        print(resultado)
else:
    print(resultado)