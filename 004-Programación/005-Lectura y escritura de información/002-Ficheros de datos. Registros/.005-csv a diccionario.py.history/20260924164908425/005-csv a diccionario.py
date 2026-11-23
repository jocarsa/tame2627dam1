archivo = open('clientes.csv','r')
# Solo leemos la primera linea
cabecera = archivo.readline()
# Partimos la primera linea en una lista de cabeceras de columna
cabeceras = cabecera.split("|")
print(cabeceras)