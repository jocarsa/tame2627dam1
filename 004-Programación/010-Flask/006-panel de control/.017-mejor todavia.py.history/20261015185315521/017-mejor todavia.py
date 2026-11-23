import mysql.connector
from flask import Flask, render_template

aplicacion = Flask(__name__)

connection = mysql.connector.connect(
          host='localhost',
          user='tiendaonlinetame',
          password='TAME123$',
          database='tiendaonlinetame'
      )
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
nombre = "La tienda de Jose Vicente desde Python"
    piedepagina = "(c) 2026 Jose Vicente Carratala desde Python"
  
@aplicacion.route("/")
def inicio():
    
    
    return render_template(
        "tienda.html",
        enviotienda=nombre,
        enviopiedepagina=piedepagina,
     		enviolista = productos
    )
    
@aplicacion.route("/admin")
def admin():
    cursor.execute("SELECT * FROM productos;")
    productos = cursor.fetchall()
    nombre = "La tienda de Jose Vicente desde Python"
    piedepagina = "(c) 2026 Jose Vicente Carratala desde Python"
    return render_template(
        "admin.html",
        enviotienda=nombre,
        enviopiedepagina=piedepagina,
     		enviolista = productos
    )


if __name__ == "__main__":
    aplicacion.run()
    
cursor.close()
connection.close()
