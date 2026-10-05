import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host='localhost',
    user='tienda2627',
    password='TAME123$',
    database='tienda2627'
)		
cursor = connection.cursor()

cursor.execute("""
               SELECT 
                COUNT(anio),
                ciudad
                FROM pedidos2
                GROUP BY ciudad;
               """)	

filas = cursor.fetchall()

valores = []
etiquetas = []

for fila in filas:
  valores.append(fila[0])
  etiquetas.append(fila[1])
  
plt.pie([45,76,23],labels=["A","B","C"])
plt.show()

cursor.close()
connection.close()