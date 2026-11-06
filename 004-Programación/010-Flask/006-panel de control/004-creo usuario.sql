CREATE USER 'tiendaonlinetame'@'localhost' IDENTIFIED BY 'TAME123$';

GRANT USAGE ON *.* TO 'tiendaonlinetame'@'localhost';

ALTER USER 'tiendaonlinetame'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;


GRANT ALL PRIVILEGES ON tiendaonlinetame.* 
TO 'tiendaonlinetame'@'localhost';

FLUSH PRIVILEGES;