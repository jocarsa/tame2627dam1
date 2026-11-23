CREATE USER 'tiendazapatillas'@'localhost' IDENTIFIED BY 'TiendaZapatillas123$';

GRANT USAGE ON *.* TO 'tiendazapatillas'@'localhost';

ALTER USER 'tiendazapatillas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendazapatillas.* 
TO 'tiendazapatillas'@'localhost';

FLUSH PRIVILEGES;

EXIT;