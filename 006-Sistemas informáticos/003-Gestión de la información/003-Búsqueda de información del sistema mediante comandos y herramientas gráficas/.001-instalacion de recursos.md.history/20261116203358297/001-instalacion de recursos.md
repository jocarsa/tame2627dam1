sudo apt update


sudo apt install apache2

sudo mv index.html index.html_old

nano hola.php

sudo nano hola.php

sudo apt install php

por si acaso apache no reinicia solo
sudo service apache2 restart


permisos de carpeta
propietario puede: rwx leer, escribir, ejecutar
grupo puede: r-x leer, no escribir, ejecutar
usuario global puede: leer, no escribir, ejecutar

ls -ld carpeta 

una cosa que puedo hacer es cambiar el propietario de la carpeta:
sudo chown josevicente ejerciciophp

Define tres tipos de usuario, y tres tipos de letra
XXX YYY ZZZ
XXX = propietario
YYY = grupo al que pertenece el propietario
ZZZ = cualquier otro usuario

Ahora vamos a definir los permisos

sudo chmod 777 ejerciciophp
7 = permisos de propietario
7 = permisos de grupo
7 = permisos de cualquier usuario

Número	Permisos	Significado
0	---	Ninguno
1	--x	Ejecución
2	-w-	Escritura
3	-wx	Escritura + ejecución
4	r--	Lectura
5	r-x	Lectura + ejecución
6	rw-	Lectura + escritura
7	rwx	Todos los permisos

drwxr-xr-x = rwx=7 r-x5 r-x5 = 755
sudo chmod 000 ejerciciophp 


Si el propietario
1.-puede leer
2.-Puede escribir
3.-Puede ejecutar

Si el grupo
4.-puede leer
5.-puede escribir
6.-puede ejecutar

Si cualquier otro usuario
7.-puede leer
8.-puede escribir
9.-puede ejecutar

