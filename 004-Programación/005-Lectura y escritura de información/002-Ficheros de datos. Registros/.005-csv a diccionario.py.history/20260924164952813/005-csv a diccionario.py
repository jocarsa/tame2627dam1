archivo = open('clientes.csv','r')
# Solo leemos la primera linea
cabecera = archivo.readline() # Singular
# Partimos la primera linea en una lista de cabeceras de columna
cabeceras = cabecera.split("|")
# Ahora si ya lo leemos todo
lineas = archivo.readlines() # Plural
for linea in lineas