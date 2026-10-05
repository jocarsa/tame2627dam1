import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='tienda2627',
    password='TAME123$',
    database='tienda2627'
)		
cursor = connection.cursor()

cursor.execute("""
               SELECT 
                anio,
                COUNT(cliente) 
                FROM pedidos2
                GROUP BY anio;
               """)	

filas = cursor.fetchall()

for fila in filas:
  print(fila)

cursor.close()
connection.close()