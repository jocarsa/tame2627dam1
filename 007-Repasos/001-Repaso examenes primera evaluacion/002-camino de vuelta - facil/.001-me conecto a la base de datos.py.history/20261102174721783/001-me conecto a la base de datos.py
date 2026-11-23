import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='periodicodam2627',
        password='TAME123$',
        database='periodicodam2627'
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM noticias;")
noticias = cursor.fetchall()

for noticia in noticias:
  print(producto)
  
cursor.close()
connection.close()