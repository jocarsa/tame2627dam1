sudo mysql -u root -p

CREATE DATABASE blogdamtame2627;

USE blogdamtame2627;

CREATE TABLE articulos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha DATE,
  contenido TEXT
);

INSERT INTO articulos (titulo, fecha, contenido) VALUES
(
  'JOCARSA: soluciones tecnológicas para empresas',
  '2026-10-26',
  'JOCARSA es una iniciativa especializada en el desarrollo de software, aplicaciones empresariales, inteligencia artificial y formación tecnológica. Nuestro objetivo es crear soluciones prácticas que ayuden a las empresas a digitalizar sus procesos y mejorar su productividad.'
),
(
  'El futuro de JOCARSA pasa por la inteligencia artificial',
  '2026-10-25',
  'En JOCARSA estamos ampliando nuestro catálogo de productos y servicios para incorporar inteligencia artificial a los procesos empresariales. Apostamos por soluciones útiles, sostenibles y adaptadas a las necesidades reales de cada organización.'
),
(
  'Aplicaciones empresariales desarrolladas a medida',
  '2026-10-24',
  'Una de las principales actividades de JOCARSA es el desarrollo de aplicaciones personalizadas. Creamos herramientas para gestionar clientes, empleados, proyectos, documentos, comunicaciones y procesos administrativos mediante tecnologías web modernas.'
),
(
  'JOCARSA y la inteligencia artificial local',
  '2026-10-23',
  'Nuestra apuesta por la inteligencia artificial local permite ejecutar modelos de lenguaje en infraestructura propia. Esta estrategia facilita el control de la información, la personalización de los modelos y la integración de capacidades inteligentes en aplicaciones empresariales.'
),
(
  'JOCARSA Ventas: gestión comercial y CRM',
  '2026-10-22',
  'JOCARSA Ventas es una aplicación diseñada para organizar la actividad comercial de una empresa. Permite gestionar contactos, clientes, campañas, productos, empleados y oportunidades de venta, incorporando estadísticas de conversión y herramientas de seguimiento comercial.'
),
(
  'JOCARSA Formación: tecnología al servicio del aprendizaje',
  '2026-10-21',
  'La plataforma JOCARSA Formación reúne herramientas para facilitar el aprendizaje de programación y tecnologías digitales. Incluye recursos educativos, actividades prácticas, seguimiento del alumnado, evaluaciones y funcionalidades para mejorar la experiencia formativa.'
),
(
  'JOCARSA Proyectointermodular: gestión de proyectos educativos',
  '2026-10-20',
  'JOCARSA Proyectointermodular facilita la planificación y seguimiento de proyectos académicos. Permite organizar grupos, módulos profesionales, resultados de aprendizaje, entregas y plazos, proporcionando una visión completa del progreso de cada estudiante.'
),
(
  'JOCARSA Arquitectura: diseño técnico desde el navegador',
  '2026-10-19',
  'JOCARSA Arquitectura es una herramienta de diseño bidimensional que permite crear planos, distribuir espacios, incorporar mobiliario y representar instalaciones eléctricas. Su interfaz web facilita la edición de proyectos técnicos sin depender de programas de escritorio tradicionales.'
),
(
  'JOCARSA Dictado: transcripción inteligente de audio',
  '2026-10-18',
  'JOCARSA Dictado combina reconocimiento de voz e inteligencia artificial para convertir grabaciones en documentos de texto. Mediante modelos de transcripción y procesamiento lingüístico, permite transformar contenido hablado en información estructurada y reutilizable.'
),
(
  'JOCARSA Cuaderno: evaluación y seguimiento académico',
  '2026-10-17',
  'JOCARSA Cuaderno es una aplicación orientada al profesorado que facilita la gestión de calificaciones, actividades y evaluaciones. Su sistema de ponderaciones y organización visual permite analizar el rendimiento del alumnado de forma sencilla.'
),
(
  'JOCARSA Cuestionarios: evaluación digital interactiva',
  '2026-10-16',
  'JOCARSA Cuestionarios permite crear y administrar pruebas de evaluación mediante una interfaz web. Incorpora herramientas de gestión de usuarios, resultados, estadísticas e informes que ayudan a conocer el progreso de los participantes.'
),
(
  'JOCARSA Prácticas: conexión entre estudiantes y empresas',
  '2026-10-15',
  'JOCARSA Prácticas facilita la organización de las prácticas formativas en empresas. Permite gestionar estudiantes, organizaciones colaboradoras, grupos y asignaciones, incorporando herramientas geográficas para analizar distancias y ubicaciones.'
),
(
  'JOCARSA Red: una red social profesional propia',
  '2026-10-14',
  'JOCARSA Red es una plataforma social orientada a conectar profesionales y compartir conocimientos. Incluye perfiles personales, publicaciones, categorías, contactos y herramientas para descubrir contenidos de otros usuarios.'
),
(
  'JOCARSA ERP: integración de la gestión empresarial',
  '2026-10-13',
  'El proyecto JOCARSA ERP busca centralizar diferentes procesos de administración empresarial en una única plataforma. Su arquitectura modular permite incorporar funcionalidades, gestionar permisos y organizar la información de manera estructurada.'
),
(
  'JOCARSA Asistencias: control de presencia digital',
  '2026-10-12',
  'JOCARSA Asistencias es una herramienta para registrar y consultar la presencia de usuarios en actividades y sesiones. Ofrece funciones de administración, importación de datos y seguimiento mediante una interfaz sencilla.'
),
(
  'JOCARSA Kanban: organización visual del trabajo',
  '2026-10-11',
  'JOCARSA Kanban permite organizar tareas y proyectos mediante tableros visuales. Su estructura basada en columnas y categorías facilita el seguimiento de actividades, la identificación de prioridades y la planificación del trabajo.'
),
(
  'JOCARSA Video: una experiencia audiovisual personalizada',
  '2026-10-10',
  'JOCARSA Video es un reproductor multimedia desarrollado para ofrecer funciones avanzadas de reproducción, subtítulos y navegación temporal. Está orientado especialmente a contenidos formativos y a la integración con plataformas educativas.'
),
(
  'Automatización de procesos mediante herramientas JOCARSA',
  '2026-10-09',
  'En JOCARSA desarrollamos soluciones para reducir tareas repetitivas y mejorar la eficiencia operativa. La automatización de documentos, importaciones, informes, comunicaciones y operaciones administrativas permite dedicar más tiempo a actividades de mayor valor.'
),
(
  'El ecosistema tecnológico de JOCARSA',
  '2026-10-08',
  'El catálogo de JOCARSA incluye aplicaciones para gestión empresarial, educación, productividad, comunicación y creación de contenidos. Nuestro enfoque consiste en desarrollar herramientas especializadas que puedan integrarse mediante servicios web y APIs.'
),
(
  'JOCARSA: innovación, desarrollo y formación tecnológica',
  '2026-10-07',
  'La filosofía de JOCARSA combina experiencia en programación, desarrollo de productos propios y formación tecnológica. Seguimos trabajando en nuevas herramientas y soluciones basadas en inteligencia artificial para responder a los retos de transformación digital de empresas y profesionales.'
);


CREATE USER 'blogdamtame2627'@'localhost' IDENTIFIED BY 'TAME123$';

GRANT USAGE ON *.* TO 'blogdamtame2627'@'localhost';

ALTER USER 'blogdamtame2627'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;


GRANT ALL PRIVILEGES ON logintame.* 
TO 'logintame'@'localhost';

FLUSH PRIVILEGES;
