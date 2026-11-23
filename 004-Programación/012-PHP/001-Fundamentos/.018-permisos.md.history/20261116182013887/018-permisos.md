En linux la carpeta de publicación está muy protegida, por ataques

ENTONCES:

Si estáis en VUESTRO propio ordenador, y por lo tanto apache no está en producción sino en desarrollo:

Levantaís los permisos al máximo de la carpeta de publicación:

sudo chmod 777 -R /var/www/html
(esto te da permisos para crear carpetas y archivos en TU apache)

SOLO para equipo de desarrollo
Cuando esto sea en servidor de producción NO hay que poner 777 sino que en sistemas informáticos os diré lo que hay que poner