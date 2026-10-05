import json

archivo = open("misdatos.json", 'r')
contenido = json.load(archivo)
print(contenido)