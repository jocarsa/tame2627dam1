import mysql.connector												# Impporto conector

connection = mysql.connector.connect(
        host='localhost',
        user='blogexamen2627',
        password='TAME123$',
        database='blogexamen2627'
    )																					# Me conecto a la base de datos
cursor = connection.cursor()									# Creo un cursor para hacer peticiones
cursor.execute("SELECT * FROM noticias;")			# Selecciono todo de noticias
noticias = cursor.fetchall()									# Lo meto todo en un array

for noticia in noticias:											# Para cada una de las noticias
  print(noticia)															# Imprimo la noticia
  
cursor.close()																# Cierro el cursor
connection.close()														# Cierro la conexión