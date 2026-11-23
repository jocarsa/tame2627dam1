import os

ruta = "/var/www/html/tame2627dam1"

with open("arbol.txt", "w") as salida:

    for carpeta, carpetas, archivos in os.walk(ruta):
        salida.write(carpeta + "\n")

        for archivo in archivos:
            salida.write("  - " + archivo + "\n")

print("Tree saved to arbol.txt")