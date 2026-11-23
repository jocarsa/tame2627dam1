from flask import Flask
import mysql.connector

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return "Esto marcha"
  
if __name__ == "__main__":
  aplicacion.run()