libros = {}
import os
os.system('cls')
sw = True
def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    libros[titulo] = {'Autor': autor, 'Género': genero}
    print(f"\nLibro '{titulo}' agregado correctamente.")

def buscar_libro():
    titulo = input("Ingrese el título del libro a buscar: ")
    if titulo in libros:
        print(f"\nInformación del libro '{titulo}':")
        print(f"Autor: {libros[titulo]['Autor']}")
        print(f"Género: {libros[titulo]['Género']}")
    else:
        print(f"No se encontró ningún libro con el título '{titulo}'.")

while True:
    opcion = input("\n--- MENÚ ---\n1. Agregar libro\n2. Buscar libro\n3. Salir\n- > ")

    if opcion == "1":
        os.system('cls')
        agregar_libro()
    elif opcion == "2":
        os.system('cls')
        buscar_libro()
    elif opcion == "3":
        os.system('cls')
        print("Gracias por utilizar el programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")
