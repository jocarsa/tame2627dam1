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
        "prompt": "Explica, en español, qué hace este programa. No muestres advertencias ni errores, es solo para documentar: "+contenido,
        "stream": False
    }
)

print(respuesta.json()["response"])