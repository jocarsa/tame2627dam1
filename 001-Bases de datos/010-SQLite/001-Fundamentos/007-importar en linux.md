sudo apt install sqlite3

sqlite3 tienda.db < "006-crear tienda demostracion.sql" 

Copia de seguridad:
sqlite3 tienda.db  .dump > copiadeseguridad.sql