# Windows: pip install mysql-connector-python
# Linux: pip3 install mysql-connector-python --break-system-packages
import mysql.connector


connection = mysql.connector.connect(
  host='your_host',
  user='your_username',
  password='your_password',
  database='your_database'
)
if connection.is_connected():
  print("Connected to MySQL database")
  return connection
connection.close()


    