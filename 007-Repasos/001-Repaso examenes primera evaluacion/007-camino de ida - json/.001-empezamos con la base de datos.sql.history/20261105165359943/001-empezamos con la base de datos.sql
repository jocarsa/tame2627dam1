sudo mysql -u root -p

CREATE DATABASE blogexamen2627;
USE blogexamen2627;

CREATE TABLE noticias(
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha DATE,
  contenido TEXT
);


INSERT INTO noticias (titulo, fecha, contenido) VALUES
('Jocarsa presenta su nueva plataforma de desarrollo empresarial',
'2026-11-05',
'Jocarsa anuncia una nueva plataforma para desarrollar aplicaciones empresariales de forma rápida y eficiente. La solución integra herramientas de administración, gestión de usuarios, bases de datos y generación automática de interfaces.'),

('Jocarsa apuesta por la inteligencia artificial local',
'2026-11-03',
'La compañía continúa investigando soluciones de inteligencia artificial ejecutadas en servidores propios. Esta estrategia permite reducir la dependencia de servicios externos y mantener un mayor control sobre los datos.'),

('Nueva versión del motor Jocarsa Base de Datos',
'2026-11-01',
'Jocarsa presenta mejoras en su motor de bases de datos desarrollado en C++. La actualización incorpora nuevos tipos de datos, almacenamiento optimizado y mecanismos de compatibilidad con versiones anteriores.'),

('Jocarsa desarrolla un sistema de informes dinámicos',
'2026-10-29',
'El nuevo generador de informes permite crear documentos profesionales a partir de información almacenada en bases de datos. Incluye tablas, gráficos, estadísticas y herramientas de exportación.'),

('La formación tecnológica sigue creciendo en Jocarsa',
'2026-10-26',
'Jocarsa amplía sus contenidos educativos relacionados con programación, desarrollo web, bases de datos y administración de sistemas. Los materiales combinan explicaciones teóricas y ejercicios prácticos.'),

('Jocarsa incorpora nuevas herramientas de automatización',
'2026-10-23',
'Las nuevas funcionalidades permiten automatizar procesos administrativos repetitivos. Los usuarios pueden configurar operaciones para reducir tareas manuales y mejorar la productividad.'),

('Nueva interfaz para gestionar aplicaciones empresariales',
'2026-10-20',
'Jocarsa presenta una interfaz renovada con navegación mediante tablas, tarjetas y estructuras jerárquicas. El diseño prioriza la claridad visual, la accesibilidad y la adaptación a diferentes dispositivos.'),

('Jocarsa investiga modelos de lenguaje de código abierto',
'2026-10-17',
'El equipo técnico experimenta con diferentes modelos de inteligencia artificial que pueden ejecutarse localmente. El objetivo es evaluar su capacidad para generar código, responder consultas y analizar documentos.'),

('La plataforma Jocarsa incorpora gestión documental',
'2026-10-14',
'Una nueva solución permite organizar documentos digitales en colecciones y carpetas. El sistema facilita la clasificación, búsqueda y recuperación de información mediante estructuras flexibles.'),

('Jocarsa mejora la seguridad de sus aplicaciones',
'2026-10-11',
'Las últimas actualizaciones incorporan controles de acceso, registros de actividad y mecanismos de protección frente a solicitudes abusivas. La seguridad continúa siendo una prioridad en el desarrollo.'),

('Jocarsa presenta un sistema avanzado de calificaciones',
'2026-10-08',
'La nueva aplicación facilita la gestión académica de alumnos, profesores, grupos y asignaturas. Incluye diferentes niveles de permisos, estadísticas y herramientas de exportación.'),

('La inteligencia artificial transforma los proyectos de Jocarsa',
'2026-10-05',
'La incorporación de modelos inteligentes permite explorar nuevas formas de crear aplicaciones, generar documentación y automatizar procesos de programación.'),

('Jocarsa desarrolla nuevas herramientas para profesores',
'2026-10-02',
'Los docentes podrán utilizar aplicaciones destinadas a organizar clases, gestionar actividades y realizar un seguimiento del progreso académico de los estudiantes.'),

('Nuevo panel de estadísticas para aplicaciones Jocarsa',
'2026-09-29',
'El sistema incorpora indicadores de rendimiento, gráficos interactivos y análisis de actividad. Los administradores pueden consultar información relevante desde un único panel.'),

('Jocarsa mejora sus servicios de videoconferencia',
'2026-09-26',
'La plataforma de videoconferencias recibe mejoras orientadas a optimizar las comunicaciones, gestionar participantes y facilitar la grabación de sesiones.'),

('Jocarsa experimenta con bases de datos documentales',
'2026-09-23',
'El proyecto explora nuevas estructuras de almacenamiento basadas en documentos JSON. Estas soluciones complementan los sistemas relacionales tradicionales.'),

('Nueva herramienta para gestionar prácticas profesionales',
'2026-09-20',
'Jocarsa desarrolla una aplicación que permite registrar contactos con empresas, entrevistas y solicitudes de prácticas. El sistema facilita el seguimiento de cada estudiante.'),

('Jocarsa amplía su biblioteca de componentes web',
'2026-09-17',
'La nueva colección incluye formularios, tablas, calendarios y componentes reutilizables. Su objetivo es acelerar la construcción de interfaces web.'),

('El desarrollo con Python gana protagonismo en Jocarsa',
'2026-09-14',
'Python continúa siendo una tecnología fundamental en los proyectos de automatización, inteligencia artificial y servicios web desarrollados dentro del ecosistema Jocarsa.'),

('Jocarsa incorpora herramientas de exportación CSV',
'2026-09-11',
'Las aplicaciones empresariales incorporan nuevas opciones para exportar e importar información en formato CSV, facilitando el intercambio de datos con otras plataformas.'),

('Nueva arquitectura modular para aplicaciones empresariales',
'2026-09-08',
'Jocarsa trabaja en una arquitectura que separa la presentación, la lógica de negocio y el almacenamiento. Esta organización facilita el mantenimiento y la evolución de las aplicaciones.'),

('Jocarsa investiga la generación automática de código',
'2026-09-05',
'Los experimentos combinan modelos de lenguaje con herramientas de desarrollo para generar estructuras HTML, CSS, JavaScript y Python a partir de instrucciones escritas.'),

('El ecosistema Jocarsa incorpora nuevas API',
'2026-09-02',
'Los servicios desarrollados permiten conectar diferentes aplicaciones mediante interfaces HTTP y respuestas JSON. La integración facilita el intercambio de información.'),

('Jocarsa presenta mejoras en sus formularios dinámicos',
'2026-08-30',
'Los formularios pueden construirse automáticamente a partir de definiciones de datos. El sistema interpreta tipos de campos y genera controles adecuados para cada información.'),

('Nueva herramienta para visualizar estructuras de datos',
'2026-08-27',
'Jocarsa presenta una solución para representar información mediante tablas, árboles y tarjetas. Los usuarios pueden elegir la visualización más adecuada para cada conjunto de datos.'),

('Jocarsa apuesta por tecnologías web abiertas',
'2026-08-24',
'HTML5, CSS3 y JavaScript continúan formando parte de la estrategia tecnológica de Jocarsa. Estas tecnologías permiten crear aplicaciones compatibles con navegadores modernos.'),

('La accesibilidad se convierte en una prioridad',
'2026-08-21',
'Las nuevas interfaces incorporan mejoras de contraste, navegación por teclado y adaptación a diferentes tamaños de pantalla para facilitar su utilización.'),

('Jocarsa desarrolla nuevas soluciones con PHP',
'2026-08-18',
'PHP sigue siendo una de las tecnologías utilizadas para construir servicios empresariales, aplicaciones educativas y herramientas de administración web.'),

('Nueva generación de paneles administrativos',
'2026-08-15',
'Jocarsa trabaja en paneles de administración que integran gestión de usuarios, permisos, informes, estadísticas y configuración avanzada.'),

('Jocarsa mejora la integración entre Python y C++',
'2026-08-12',
'El desarrollo de conectores permite acceder desde Python a funcionalidades implementadas en C++. Esta combinación busca aprovechar la facilidad de programación y el rendimiento de ambos lenguajes.'),

('Jocarsa explora aplicaciones de inteligencia artificial educativa',
'2026-08-09',
'Los nuevos prototipos utilizan inteligencia artificial para apoyar la creación de materiales didácticos, resolver dudas y facilitar ejercicios de programación.'),

('Nueva herramienta de seguimiento de actividad',
'2026-08-06',
'Las aplicaciones incorporan registros que permiten consultar operaciones realizadas por los usuarios. Esta información facilita las auditorías y el diagnóstico de incidencias.'),

('Jocarsa investiga sistemas de búsqueda semántica',
'2026-08-03',
'El equipo experimenta con embeddings y bases de datos vectoriales para encontrar documentos mediante similitud de significado en lugar de coincidencias exactas.'),

('Las aplicaciones Jocarsa mejoran su rendimiento',
'2026-07-31',
'Las optimizaciones recientes buscan reducir tiempos de carga, consultas innecesarias y consumo de recursos en servidores y navegadores.'),

('Jocarsa desarrolla un gestor de proyectos inteligente',
'2026-07-28',
'La nueva plataforma permite organizar proyectos, conversaciones e iteraciones de desarrollo. El objetivo es conservar el historial de trabajo y facilitar modificaciones posteriores.'),

('Nuevas herramientas de administración de servidores',
'2026-07-25',
'Jocarsa experimenta con utilidades para analizar registros de Apache, revisar procesos activos y supervisar el estado de servicios alojados en Linux.'),

('Jocarsa impulsa el aprendizaje práctico de SQL',
'2026-07-22',
'Los nuevos ejercicios educativos permiten practicar consultas SELECT, INSERT, UPDATE y DELETE sobre bases de datos con información de ejemplo.'),

('Nueva biblioteca de gráficos para informes',
'2026-07-19',
'El sistema de informes incorpora visualizaciones de barras, líneas, sectores, indicadores y otros formatos destinados al análisis de datos.'),

('Jocarsa investiga nuevas aplicaciones de WebSocket',
'2026-07-16',
'Los prototipos de comunicación en tiempo real permiten intercambiar mensajes entre navegadores y servidores sin realizar consultas HTTP continuas.'),

('La automatización documental avanza en Jocarsa',
'2026-07-13',
'Las herramientas experimentales permiten generar documentos estructurados a partir de plantillas e información procedente de aplicaciones empresariales.'),

('Jocarsa incorpora calendarios interactivos',
'2026-07-10',
'Los nuevos componentes permiten visualizar actividades mediante vistas anuales, mensuales, semanales y diarias, facilitando la planificación de tareas.'),

('Nuevas herramientas para importar información empresarial',
'2026-07-07',
'Jocarsa desarrolla mecanismos de importación capaces de incorporar datos externos, detectar registros duplicados y facilitar procesos de actualización.'),

('Jocarsa estudia nuevas técnicas de almacenamiento',
'2026-07-04',
'Las investigaciones se centran en optimizar el espacio utilizado por los registros y adaptar el almacenamiento al tamaño real de los distintos tipos de datos.'),

('La personalización visual llega a nuevas aplicaciones',
'2026-07-01',
'Los usuarios pueden ajustar colores, transparencias y determinadas características de presentación para adaptar las interfaces a sus preferencias.'),

('Jocarsa desarrolla soluciones de comunicación en red',
'2026-06-28',
'Los nuevos ejemplos técnicos incluyen servidores TCP, clientes Python y sistemas de intercambio de mensajes entre múltiples dispositivos.'),

('Nuevas funcionalidades para la gestión de usuarios',
'2026-06-25',
'Las aplicaciones incorporan mecanismos de autenticación, perfiles diferenciados y controles de permisos para administrar el acceso a la información.'),

('Jocarsa amplía sus contenidos de programación',
'2026-06-22',
'Los nuevos materiales incluyen ejercicios sobre estructuras de datos, programación orientada a objetos, desarrollo de interfaces y conexión con bases de datos.'),

('La integración de IA y bases de datos abre nuevas posibilidades',
'2026-06-19',
'Jocarsa experimenta con sistemas capaces de interpretar preguntas en lenguaje natural y convertirlas en consultas estructuradas sobre información empresarial.'),

('Jocarsa presenta mejoras en sus herramientas de desarrollo',
'2026-06-16',
'Las nuevas versiones buscan simplificar operaciones habituales, reutilizar componentes y facilitar la creación de aplicaciones completas.'),

('Jocarsa prepara nuevas experiencias de desarrollo inteligente',
'2026-06-13',
'El proyecto continúa explorando una plataforma que permita describir aplicaciones mediante lenguaje natural y obtener prototipos funcionales con ayuda de inteligencia artificial.');

