mysqldump -u root -p dam1 > backupmanual.sql

para restaurar:

primero creas una base de datos vacia:
sudo mysql -u root -p

Ahora creo una base de datos de recuperacion
CREATE DATABASE recuperacion;
SHOW TABLES;

