from flask import Flask,render_template, jsonify
import mysql.connector

aplicacion = Flask(__name__)

connection = mysql.connector.connect(
        host='localhost',
        user='blogdamtame2627',
        password='TAME123$',
        database='blogdamtame2627'
    )
cursor = connection.cursor(dictionary=True)

@aplicacion.route("/")
def inicio():
  return render_template("blog.html")

@aplicacion.route("/articulos")
def articulos():
  # Ahora me conecto a la base de datos y te doy los articulos
  cursor.execute("SELECT * FROM articulos;")
  articulos = cursor.fetchall()
  return jsonify(articulos)
  

if __name__ == "__main__": 
  aplicacion.run()

