from flask import Flask,render_template,request
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaexamen',
        password='TAME123$',
        database='tiendaexamen'
    )
cursor = connection.cursor(dictionary=True)

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
	cursor.execute("SELECT * FROM productos;")
	productos = cursor.fetchall()
	return render_template("front.html",productos=productos)

@aplicacion.route("/insertar",methods=['POST'])
def insertar():
	return "ok"

@aplicacion.route("/admin")
def admin():
	return render_template("admin.html")
  
if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()