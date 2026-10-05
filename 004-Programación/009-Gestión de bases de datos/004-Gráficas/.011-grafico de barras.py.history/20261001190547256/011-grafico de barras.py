import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host='localhost',
    user='tienda2627',
    password='TAME123$',
    database='tienda2627'
)		

colores = [
    "#1E3A5F",  # azul muy oscuro
    "#6BAED6",  # azul claro
    "#285F8F",  # azul oscuro
    "#9ECAE1",  # azul muy claro
    "#377EB8",  # azul medio
    "#C6DBEF",  # azul pálido
    "#174A73",  # azul profundo
    "#7FB8DA",  # azul luminoso
    "#3F78A8",  # azul medio oscuro
    "#B3D5E8"   # azul pastel
]

cursor = connection.cursor()

cursor.execute("""
               SELECT 
                COUNT(anio),
                ciudad
                FROM pedidos2
                GROUP BY ciudad
                ORDER BY ciudad DESC;
               """)	

filas = cursor.fetchall()

valores = []
etiquetas = []

for fila in filas:
  valores.append(fila[0])
  etiquetas.append(fila[1])
  
plt.bar(etiquetas,valores)
plt.show()

cursor.close()
connection.close()