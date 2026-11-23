CREATE USER 
'programacion2627'@'localhost' 
IDENTIFIED  BY 'TAME123$';

GRANT USAGE ON *.* TO 'programacion2627'@'localhost';


-- quitale todos los limites que tenga
ALTER USER '[tunombredeusuario]'@'[tuservidor]' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

ALTER USER 'josevicente2627'@'localhost' 
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