# Convertir Proyecto Python a .EXE

1. Tener instalado en nuestra maquina el interprete de Python
2. Tener pip instalado en nuentra maquina
3. Tenerlo añadido al path
4. Instalar PyInstaller por consola de con pip
5. "pip install pyinstaller"
6. [Enlace a la documentacion oficial de PyInstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html)
7. Nos situamos en la carpeta del proyecto con el codigo que deseamos empaquetar
8. Escribimos en la consola pyinstaller --onefile nombredelscript.py
9. El --onefile es para juntar todo lo de tu proyecto en el .exe sin el solo expaqueta el script
10. [La informacion la extraje](https://parzibyte.me/blog/2018/03/23/empaquetando-python-generar-archivo-exe/)
11. Añadir al .spec la ruta de los archivos que deseamos empaquetar
12. Para empquetar archivos externos al proyecto necesitaremos pyinstaller --onefile <nombredelarchivo>.spec
13. [La informacion la extraje](https://parzibyte.me/blog/2018/12/27/pyinstaller-assets-imagenes-archivos-ejecutable-python/)