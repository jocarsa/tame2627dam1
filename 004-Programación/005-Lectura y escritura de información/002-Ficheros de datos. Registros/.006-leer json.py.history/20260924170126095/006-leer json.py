import json

archivo = open("misdatos.json", 'r')
contenido = json.loads(archivo)
print(contenido)