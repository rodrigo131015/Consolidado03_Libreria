#Importamos las funciones 
from Funciones import agregar_actualizarLibro, venderLibro, buscarLibro, eliminarLibro, listarLibros
#Funcion menu
def menu():
    libreria = {}
    while True:
        #Creamos un menu 
        print("========= Libreria Continental ==========")
        print("1. Agregar/Actualizar libro")
        print("2. Vender libro")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Listar libros")
        print("6. Salir")
        #Pedimos al usuario la opcion a elegir
        op = input("Ingrese opcion: ").strip()
        #Ingresamos nombre y cantidad del libro a añadir o actualizar
        if op == "1":
            nombre = input("Ingrese nombre de libro: ").strip().capitalize()
            cantidad = int(input("cantidad de libros a ingresar/actulizar: "))
            nuevo = agregar_actualizarLibro(libreria, nombre, cantidad)
            print("OK:", nombre, "=", nuevo)
        #Ingresamos nombre del libro a vender y llamamos a la funcion vender
        elif op == "2":
            nombre = input("Ingrese nombre de libro a vender: ").strip().capitalize()
            ok, quedan = venderLibro(libreria, nombre)
            if ok:
                print("Vendido 1. Queda:", quedan)
            else:
                print("Stock insuficiente.")
        #
        elif op == "3":
            nombre = input("Ingrese nombre de libro a buscar: ").strip().capitalize()
            dato = buscarLibro(libreria, nombre)
            if dato is not None:
                print(nombre, "->", dato)
            else:
                print("Libro inexistente.")
        elif op == "4":
            nombre = input("Ingrese nombre de libro a eliminar: ").strip().capitalize()
            if eliminarLibro(libreria, nombre):
                print("Libro eliminado.")
            else:
                print("Libro inexistente.")
        elif op == "5":
            items = listarLibros(libreria)
            if not items:
                print("Inventario vacio.")
            else:
                for i, j in items:
                    print(f"- {i}: {j}")
        elif op == "6":
            salir = input("Seguro que desea salir (SI/NO): ").upper()
            if salir == "SI":
                print("Saliendo del programa......")
                break
        else:
            print("Opcion invalida. Intentelo de nuevo")
menu()



