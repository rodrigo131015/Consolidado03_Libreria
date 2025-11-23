#Creamos las funciones a utilizar
#Funcion agregar / actualizar libro
def agregar_actualizarLibro(libreria, nombre, cantidad):
    libreria[nombre] = libreria.get(nombre, 0) + cantidad
    return libreria[nombre]
#Funcion vender libro
def venderLibro(libreria, nombre):
    if libreria.get(nombre, 0) > 0:
        libreria[nombre] -= 1
        return True, libreria[nombre]
    else:
        return False, 0
#Funcion buscar libro
def buscarLibro(libreria, nombre):
    return libreria.get(nombre, None)
#Funcion eliminiar libro
def eliminarLibro(libreria, nombre):
    if nombre in libreria:
        del libreria[nombre]
        return True
    else:
        return False
#Funcion listar libros
def listarLibros(libreria):
    return list(libreria.items())