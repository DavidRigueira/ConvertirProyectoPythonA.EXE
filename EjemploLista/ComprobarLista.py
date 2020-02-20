def agregarNombre(lista, nombre):
    if nombre: lista.append(nombre)
    return lista
 
def buscarNombre(lista, nombre):
    return nombre in lista
 
def posicionNombre(lista, nombre):
    return [i+1 for i in range(len(lista)) if nombre==lista[i]]
 
def totalNombres(lista):
    return len(lista)
 
def contarNombre(lista, nombre):
    cantidad=len([x for x in lista if x == nombre])
    return cantidad
 
def borrarNombre(lista,nombre):
    try:
        lista.remove(nombre)
        return (lista, True)
    except:
        pass
    return (lista, False)
 
def mostrarNombres(lista):
    if (totalNombres(lista)):
        print("Los nombre que hay en la lista son: {}".format(", ".join(lista)))
    else:
        print("No hay nombre en la lista")
 
def Menú():
    print("---------------------------------------------------------------")
    print ("¿Qué quieres hacer? ")
    print ("\t1 - Añadir un nombre")
    print ("\t2 - Buscar un nombre")
    print ("\t3 - Buscar las posiciones de entrada de un nombre")
    print ("\t4 - Contar las veces que aparece un nombre")
    print ("\t5 - Borrar un nombre")
    print ("\t6 - Mostrar el total de nombres")
    print ("\t7 - Mostrar todos los nombres")
    print ("\n\t8 - Salir")
 
lista=[]
 
#PROGRAMA
while True:
    Menú ()
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion=0
 
    if opcion == 1:
        nombre = input("Ingrese el nombre a añadir: ")
        lista=agregarNombre(lista, nombre)
 
 
    elif opcion == 2:
        nombre = input("Ingrese el nombre que deseas buscar: ")
        if buscarNombre(lista, nombre):
            print(f'Se encontró el nombre: {nombre}')
        else:
            print(f'NO se encontró el nombre: {nombre}')
 
 
    elif opcion == 3:
        nombre = input("Ingrese el nombre que deseas obtener sus posiciones: ")
        if buscarNombre(lista, nombre):
            print('El {} se encuentra en las posiciones: {}'.format(nombre, ", ".join(map(str, posicionNombre(lista, nombre)))))
        else:
            print(f'NO se encuentra el nombre: {nombre}')
 
 
    elif opcion == 4:
        nombre = input("Ingrese el nombre para ver la cantidad de apariciones que tiene: ")
        cantidad=contarNombre(lista, nombre)
        if cantidad==0:
            print(f'NO se encuentra el nombre: {nombre}')
        else:
            print('El nombre {} aparece {} {}'.format(nombre, cantidad, "vez" if cantidad==1 else "veces"))
 
 
    elif opcion == 5:
        nombre = input("Ingrese el nombre que deseas borrar: ")
        (lista, eliminado) = borrarNombre(lista, nombre)
        if eliminado:
            print (f'Se ha eliminado el nombre {nombre}')
        else:
            print (f'No existe el nombre {nombre}')
 
 
    elif opcion == 6:
        cantidad=totalNombres(lista)
        print(f'El total de nombres es: {cantidad}')
 
 
    elif opcion == 7:
        mostrarNombres(lista)
 
 
    elif opcion == 8:
        print("ADIOS")
        break
 
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")