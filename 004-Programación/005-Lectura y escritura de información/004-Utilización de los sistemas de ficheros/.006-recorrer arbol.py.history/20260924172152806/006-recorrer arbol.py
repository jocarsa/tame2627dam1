import os

arbol = os.walk("/var/www/html/tame2627dam1")

for carpeta, carpetas, archivos in arbol:
    print("Carpeta actual:", carpeta)

    print("Subcarpetas:")
    for subcarpeta in carpetas:
        print("  📁", subcarpeta)

    print("Archivos:")
    for archivo in archivos:
        print("  📄", archivo)

    print()