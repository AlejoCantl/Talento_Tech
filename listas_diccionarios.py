# Lista de nombres de estudiantes
estudiantes = ["Alejo", "Kevin", "David", "Junior", "Matthews"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")

# Diccionario de información de contacto
contactos = {"Alejo": "alejo@email.com" 
             ,"Kevin":"kevin@email.com" 
             }

for clave, valor in contactos.items():
    print(f"Nombre: {clave}, Correo: {valor}")

# Script para agregar elementos a una lista o actualizar un diccionario
nuevo_estudiante = input("""Introduce el nombre de un nuevo estudiante: \n""")
estudiantes.append(nuevo_estudiante)
print("Lista actualizada de estudiantes:", estudiantes)

nuevo_contacto = input("""Introduce un nombre para actualizar/agregar: \n""")
nuevo_correo = input(f"""Introduce un correo para {nuevo_contacto}: \n""")
contactos[nuevo_contacto] = nuevo_correo
print("Contactos actualizados:", contactos)