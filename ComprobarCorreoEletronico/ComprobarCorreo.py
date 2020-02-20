import re
 
print("Escriba el correo a comprobar por ejemplo : nombre@dominio.ext")
correo = input("Ingrese el correo a comprobar: ")
##correo='nombre@dominio.ext'
 
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
	print("Correo correcto")
else:
	print("Correo incorrecto")