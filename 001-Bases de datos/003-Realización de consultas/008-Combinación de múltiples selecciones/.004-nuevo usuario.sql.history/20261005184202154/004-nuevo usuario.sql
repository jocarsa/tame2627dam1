
CREATE USER 'tiendazapatillas'@'localhost' IDENTIFIED BY 'TiendaZapatillas123$';

GRANT USAGE ON *.* TO 'tiendazapatillas'@'localhost';

ALTER USER 'tiendazapatillas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON [tubasededatos].* 
TO '[tunombredeusuario]'@'[tuservidor]';

GRANT ALL PRIVILEGES ON empresadam2627.* 
TO 'josevicente2627'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;