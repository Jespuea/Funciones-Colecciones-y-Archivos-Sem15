# 1. Creación de la colección de datos (Lista)
estudiantes = ["Carlos Mendoza", "María López", "Ana Torres"]

# 2. Funcionalidad para insertar/agregar datos
nuevo = input("Ingresa el nombre del estudiante a agregar: ")
estudiantes.append(nuevo)
print(f"✓ '{nuevo}' fue agregado a la lista.")

# 3. Operación básica adicional: Buscar elementos
buscar = input("\nIngresa el nombre del estudiante a buscar: ")
if buscar in estudiantes:
    print(f"🔍 Resultado: '{buscar}' SÍ está en la lista.")
else:
    print(f"❌ Resultado: '{buscar}' NO está registrado.")

# 4. Operación básica adicional: Eliminar elementos
eliminar = input("\nIngresa el nombre del estudiante a eliminar: ")
if eliminar in estudiantes:
    estudiantes.remove(eliminar)
    print(f"✓ '{eliminar}' fue eliminado.")
else:
    print(f"❌ '{eliminar}' no se encontró, la lista no sufrió cambios.")

# 5. Mostrar de forma clara la información almacenada
print("\n--- LISTA FINAL DE ESTUDIANTES ---")
for i, estudiante in enumerate(estudiantes, 1):
    print(f"{i}. {estudiante}")