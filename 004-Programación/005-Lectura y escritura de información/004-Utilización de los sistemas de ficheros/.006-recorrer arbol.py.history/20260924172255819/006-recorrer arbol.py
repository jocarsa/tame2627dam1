import os

ruta = "/var/www/html/tame2627dam1"

archivo_salida = open("arbol.txt", "w")

for carpeta, carpetas, archivos in os.walk(ruta):
    archivo_salida.write(carpeta + "\n")

    for archivo in archivos:
        archivo_salida.write("  - " + archivo + "\n")

archivo_salida.close()

print("Tree saved to arbol.txt")