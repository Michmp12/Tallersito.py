import os
os.system('cls')
sw = True
def agregar_estudiante(nombre, edad, carrera, archivo):
    with open(archivo, 'a') as file:
        file.write(f"{nombre},{edad},{carrera}\n")

def buscar_estudiante(nombre, archivo):
    with open(archivo, 'r') as file:
        for line in file:
            if nombre in line:
                return line.strip().split(',')
    return None

def main():
    archivo = "registro_estudiantes.txt"


    if not os.path.exists(archivo):
        with open(archivo, 'w'):
            pass

    while True:
        print("\n--- Menú ---")
        print("1. Agregar estudiante")
        print("2. Buscar estudiante por nombre")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            os.system('cls')
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            agregar_estudiante(nombre, edad, carrera, archivo)
            print("Estudiante agregado al registro.")

        elif opcion == '2':
            os.system('cls')
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            estudiante_encontrado = buscar_estudiante(nombre, archivo)
            if estudiante_encontrado:
                print("\nInformación del estudiante:")
                print(f"Nombre: {estudiante_encontrado[0]}")
                print(f"Edad: {estudiante_encontrado[1]}")
                print(f"Carrera: {estudiante_encontrado[2]}")
            else:
                print("El estudiante no fue encontrado en el registro.")

        elif opcion == '3':
            os.system('cls')
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
