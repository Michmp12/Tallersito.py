
inventario = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    inventario[nombre] = cantidad

def buscar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in inventario:
        print(f"La cantidad disponible de {nombre} es: {inventario[nombre]}")
    else:
        print("El producto no se encuentra en el inventario.")

while True:
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Salir del inventario")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        buscar_producto()
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción que sí sea válida para poder hacer el registro.")