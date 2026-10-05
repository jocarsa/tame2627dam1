# Windows: pip install mysql-connector-python
# Linux: pip3 install mysql-connector-python --break-system-packages
import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='programacion2627',
  password='TAME123$',
  database='programacion2627'
)
if connection.is_connected():
  print("Connected to MySQL database")
  return connection
connection.close()


    