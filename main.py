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
        #Ingresamos nombre del libro a buscar, creamos una variable dato con la cantidad que hay en stock,
        #Finalmente vemos si dato es diferente de None muestra el nombre del librp junto con su cantidad; si no imprime libro inexistente
        elif op == "3":
            nombre = input("Ingrese nombre de libro a buscar: ").strip().capitalize()
            dato = buscarLibro(libreria, nombre)
            if dato is not None:
                print(nombre, "->", dato)
            else:
                print("Libro inexistente.")
        #Ingresamos el nombre del libro a eliminar, llamamos a la funcion elimianrlibro la cual devuelve true o false
        elif op == "4":
            nombre = input("Ingrese nombre de libro a eliminar: ").strip().capitalize()
            if eliminarLibro(libreria, nombre):
                print("Libro eliminado.")
            else:
                print("Libro inexistente.")
        #Creamos una variable items y llamamos a la funcion listarLibros, luego si items esta vacion imprime "Inventario vacio", si no imprime la lista
        elif op == "5":
            items = listarLibros(libreria)
            if not items:
                print("Inventario vacio.")
            else:
                for i, j in items:
                    print(f"- {i}: {j}")
        #Preguntamos si desea salir del programa, si es asi rompe el ciclo, si no es vuelve al menu
        elif op == "6":
            salir = input("Seguro que desea salir (SI/NO): ").upper()
            if salir == "SI":
                print("Saliendo del programa......")
                break
        else:
            print("Opcion invalida. Intentelo de nuevo")
menu()



