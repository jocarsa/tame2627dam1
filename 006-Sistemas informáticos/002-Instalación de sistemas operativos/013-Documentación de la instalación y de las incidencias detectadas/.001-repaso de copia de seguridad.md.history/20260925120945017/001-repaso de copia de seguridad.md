mysqldump -u root -p dam1 > backupmanual.sql

para restaurar:

primero creas una base de datos vacia:
sudo mysql -u root -p

Ahora creo una base de datos de recuperacion
CREATE DATABASE recuperacion;
SHOW TABLES;

Ahora me salgo
exit;

Ahora vuelco la copia de seguridad a esa nueva
base de datos vacia
mysql -u root -p recuperacion < backupmanual.sql

