3 exámenes que van en pack: bases de datos, lenguajes de marcas, programación.

Yo llegaré al examen, y diré:
Tenéis que hacer un ejercicio sobre [ejemplo: tienda online: entidad: producto, campos: id, nombre, descripcion, precio]

- Bases de datos
	- Entráis en MySQL
  - Creáis una base de datos
  - Usáis la base de datos
  - Creáis la tabla correspondiente a la entidad que yo haya dicho
  - Insertáis datos de ejemplo (para esta parte concreta se puede usar IA)
  - Seleccionáis para comprobar que está ok
  - Creáis un usuario con permisos para poder conectaros desde Python
  
- Programación
	- Os aseguráis de que leeís los datos desde MySQL (mysql.connector)
  - Los imprimis en consola
  - Ahora usáis flask
  - Podéis elegir dos caminos para el camino de vuelta:
  	- Camino fácil: Pintar la plantilla mediante Flask y Jinja= render_template + {{}}
    - Camino no tan fácil: Dos endpoints, uno para plantilla, otro para JSON, y la plantilla carga datos con JSON y los pinta en HTML
  - Ahora en el camino de ida, podéis elegir también dos caminos:
  	- Camino fácil: Enviar la información mediante formularios HTML, usando request, usando methods=['POST']
    - Camino no tan fácil: Dos endpoints, uno para el "formulario", y otro para recibir datos de inserción  mediante JSON y fetch
  - En el examen de programación simplemente os aseguráis que podéis
  	- Leer de base de datos y escribir en la base de datos
    - Levantar endpoints y enviar y recibir información de lenguaje de marcas
  - Se puede usar IA solo para corregir problemas de indentación
    
- Lenguajes de marcas
	- Crear los templates necesarios para que el ejercicio funcione.
  - Ejemplo:
  	- Template de la tienda
    - Template de recibir pedido
  - Los templates tienen que ir:
  	- Con HTML en la carpeta template
    - Con CSS en la carpeta static
    - Opcionalmente con JS en la carpeta static
    
Una vez que acabáis estos tres ejercicios, tenéis una aplicación de ida y vuelta en marcha. SOLO cuando este paso esté cumplido, es cuando podéis usar la IA para
- HAcer la aplicación más estética
- Aumentar la funcionalidad del programa
Cuidado con lo que le pedís a la IA, porque lo que os de, tenéis que saber implementarlo
    
Ahora hablamos del resto de los exámenes:

- Sistemas informáticos
	- Traéis ISO de Ubuntu Server descargada
  - Creáis máquina virtual 2-4nucleos, 2-4GB RAM
  - Instaláis Ubuntu Server
  - Instaláis openssh-server
  - Os conectáis desde vuestra máquina
  - Instaláis python3-pip, mysql-server, python-flask y python-mysql.connector
  - Desplegáis la aplicación desde vuestra máquina al servidor
  - La ponéis en marcha
  - Desde vuestra máquina mostráis la aplicación funcionando en el servidor Ubuntu
  - Este examen va sin IA 
  
- Entornos de desarrollo (Desarrollo en Java + Swing en el IDE NetBeans)
	- Os pondré un problema de tipo "calculadora de IVA" (entrada de datos, cálculos, y salida)
  - Tenéis que crear un programa en Java
  - Tenéis que crear un JPanel para crear una interfaz (con el diseñador)
  - Tenéis que consumir datos de los inputs, boton de acción, y mostrar resultados
  - Recordad que no se usa MySQL en el examen de entornos
  - Este examen va sin IA 
  
- Proyecto intermodular
	- No hay examen como tal en la primera evaluación
  - Hay que entregar documento
  - Concretamente para el día del examen tenéis que tener entregados los puntos 1 y 2
  - Hay que rellenar los apartados en la aplicación proyectointermodular.jocarsa.com
  
Repetimos el plan de las próximas semanas:
- Semana que viene, repaso: hacemos los exámenes una y otra vez
- Semana siguiente (semana de los exámenes): No hay clase en las horas normales pero yo estoy en tutoría, si alguien necesita algo, o se viene, o videoconferencia, o correo, o lo que sea.
	- Exámenes viernes 13 de 16 a 21
  - Exámenes sábado 14 de 9 a 14
- Semana siguiente-siguiente: Empezamos la segunda evaluación - basada en proyectos
    
    
    
  