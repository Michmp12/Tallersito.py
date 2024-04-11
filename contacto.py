contactos = {}
import os
os.system('cls')
sw = True 


def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    contactos[nombre] = telefono
    enter = input(f'\nRegistro del contacto {telefono} realizado con éxito')


def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"El número de teléfono de {nombre} es {contactos[nombre]}")
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")
        

while sw == True:
    opcion = input('\n---MENÚ---\n1. Registrar\n2. Buscar\n3. Salir\n- >  ')

    
    if opcion == "1":
        os.system('cls')
        agregar_contacto()
    elif opcion == "2":
        os.system('cls')
        buscar_contacto()
    elif opcion == "3":
        print("Gracias por usar el programa.")
        sw = False
