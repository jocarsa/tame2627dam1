1.-Al examen traeréis descargada una ISO de Ubuntu Server 26.04
2.-Arrancáis virtualbox
3.-Máquina nueva
	recomiendo minimo 4nucleos de procesador
  recomiendo minimo 4GB RAM
  recomiendo disco a partir de 200GB
  no os olvidéis de poner la red en modo adaptador puente (NAT->Puente)
  
  el nombre de la máquina os lo diré en el examen
  
4.-Arrancamos y seguimos el proceso de instalacion
	idioma español
  no se aplica proxy
  aceptamos particion manual y automatica de los discos
  nombre, nombre de máquina y contraseña pondréis unos que os diré en el examen
  no openssh porque quiero que lo instaléis después a mano
  finalizamos instalacion y reiniciamos
  
5.-Iniciamos sesión
	ip a averiguamos la ip - 192.168.4.38
  sudo apt install openssh-server
  minizamos la máquina y sacamos un terminal en nuestro ordenador
  ssh josevicente@192.168.4.38
  
6.-Ahora instalamos servicios
	python lo tengo
  sudo apt install python3-pip
  pip3 install mysql-connector --break-system-packages
  pip3 install flask --break-system-packages
  sudo apt install mysql-server
  sudo mysql_secure_installation
  
7.-Trasladamos nuestro ejercicio al servidor
	Base de datos: recomiendo copiar y pegar de nuevo todos los comandos.
  Transferimos los archivos del examen anterior - recomiendo Filezilla
  
  
  
  
  
  
  
  