import requests

archivo = open("compilado.md",'r')

respuesta = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": "Explicame que es CSS, y explicalo en una sola frase.",
        "stream": False
    }
)

print(respuesta.json()["response"])