# Condicionales determinar si es par e impar
numero = (input("""Ingrese un numero \n"""))

if int(numero) % 2==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

# Bucle for: Iterar sobre una lista e imprimir los cuadrados de los números
print("""\n""")
lista = [1,2,3,4,5]
for i in lista:
    print(f"El numero {i} elevado al cuadrado es {i ** 2}")

# Bucle while: Solicitar repetidamente la entrada hasta que el usuario introduzca 'salir'
print("""\n""")
entrada = ""
while entrada != "salir":
    entrada = input("""Ingrese la opcion "salir" para salir \n""")
    print(f"Has introducido {entrada}")


    
    
