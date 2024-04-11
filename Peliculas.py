import os
class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año

def agregar_pelicula(peliculas, titulo, genero, año):
    peliculas[titulo] = Pelicula(titulo, genero, año)

def buscar_pelicula(peliculas, titulo):
    if titulo in peliculas:
        pelicula = peliculas[titulo]
        return f"Título: {pelicula.titulo}, Género: {pelicula.genero}, Año: {pelicula.año}"
    else:
        return "La película no se encuentra en la lista."
    
def main():
    peliculas = {}

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n1. AGREGAR PELICULA")
        print("2. BUSCAR PELICULA")
        print("3. SALIR")

        opcion = input("--- INFORMACION DE PELICULAS --- ")

        if opcion == "1":
            titulo = input("Ingrese el título de la película: ")
            genero = input("Ingrese el género de la película: ")
            año = input("Ingrese el año de la película: ")
            agregar_pelicula(peliculas, titulo, genero, año)
            print("Película agregada correctamente.")

        elif opcion == "2":
            titulo = input("Ingrese el título de la película a buscar: ")
            info_pelicula = buscar_pelicula(peliculas, titulo)
            print(info_pelicula)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        input("Presione Enter por favor para continuar...")

if __name__ == "__main__":
    main()
