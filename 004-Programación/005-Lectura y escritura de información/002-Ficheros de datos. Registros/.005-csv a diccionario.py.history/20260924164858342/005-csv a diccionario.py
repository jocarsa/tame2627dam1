archivo = open('clientes.csv','r')
# Solo leemos la primera linea
cabecera = archivo.readline()
cabeceras = cabecera.split("|")
print(cabeceras)