import requests

archivo = open("compilado.md",'r')
contenido = ""
lineas = archivo.readlines()
for linea in lineas:
  contenido += linea
  
archivo.close()

respuesta = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": "Explica qué hace este programa: "+contenido,
        "stream": False
    }
)

print(respuesta.json()["response"])