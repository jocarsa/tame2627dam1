import requests

respuesta = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": "Explicame que es CSS, y explicalo en un solo párrafo.",
        "stream": False
    }
)

print(respuesta.json()["response"])