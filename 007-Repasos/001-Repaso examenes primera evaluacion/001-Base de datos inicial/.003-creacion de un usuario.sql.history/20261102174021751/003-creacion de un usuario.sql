CREATE USER 'tiendaexamen'@'localhost' IDENTIFIED BY 'TAME123$';

GRANT USAGE ON *.* TO 'tiendaexamen'@'localhost';

ALTER USER 'tiendaexamen'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;


GRANT ALL PRIVILEGES ON tiendaexamen.* 
TO 'tiendaexamen'@'localhost';

FLUSH PRIVILEGES;