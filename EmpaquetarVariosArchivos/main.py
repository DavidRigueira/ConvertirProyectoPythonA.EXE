import  os , sys


def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

nombre_archivo = resolver_ruta("archivo.txt")
with open(nombre_archivo, "r") as archivo:
    for linea in archivo:
        print("Aquí hay una línea: ", linea)
input("Presiona Enter para salir")