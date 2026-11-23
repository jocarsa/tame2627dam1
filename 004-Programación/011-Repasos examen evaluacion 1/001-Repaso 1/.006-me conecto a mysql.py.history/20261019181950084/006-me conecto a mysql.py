import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='blog2627',
        password='Blog2627$',
        database='blog2627'
    )
cursor = connection.cursor()