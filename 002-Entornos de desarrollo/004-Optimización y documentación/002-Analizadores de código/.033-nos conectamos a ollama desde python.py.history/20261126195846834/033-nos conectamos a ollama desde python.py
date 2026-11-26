import requests

respuesta = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gpt-oss:20b",
        "prompt": "Explain what a neural network is",
        "stream": False
    }
)

print(respuesta.json()["response"])