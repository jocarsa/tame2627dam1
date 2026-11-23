import pickle

frutas = []

archivo = open('frutas.dat', 'rb')
frutas = pickle.load(archivo)
print(frutas)
archivo.close()