import datetime
archivo = open('current_datetime.txt', 'w')
current_datetime = datetime.datetime.now()
archivo.write(current_datetime.strftime('%Y-%m-%d %H:%M:%S'))
archivo.close();