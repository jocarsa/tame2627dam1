PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    marca TEXT NOT NULL,
    descripcion TEXT,
    categoria TEXT NOT NULL,
    genero TEXT NOT NULL,
    capacidad_ml INTEGER NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO productos VALUES(1,'Amanecer Dorado','Esencia Real','Fragancia fresca con notas de bergamota, jazmín y almizcle.','Floral','Mujer',100,59.9500000000000028,45,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(2,'Noche de Cristal','Luna Azul','Perfume elegante con vainilla, ámbar y flores blancas.','Oriental','Mujer',75,74.5,32,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(3,'Bosque Encantado','Raíz Noble','Aroma amaderado con cedro, pino y musgo.','Amaderado','Hombre',100,65.0,28,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(4,'Brisa Mediterránea','Costa Clara','Fragancia marina con limón, sal y lavanda.','Acuático','Unisex',100,48.8999999999999985,67,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(5,'Rosa Imperial','Esencia Real','Perfume floral de rosas, peonías y almizcle blanco.','Floral','Mujer',50,89.0,19,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(6,'Fuego Interior','Alma Salvaje','Aroma intenso de pimienta negra, cuero y madera.','Especiado','Hombre',100,79.9500000000000028,36,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(7,'Jardín Secreto','Flor de Alba','Mezcla delicada de gardenia, jazmín y magnolia.','Floral','Mujer',75,54.8999999999999985,54,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(8,'Horizonte Azul','Costa Clara','Notas frescas de océano, menta y cítricos.','Acuático','Hombre',100,62.5,41,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(9,'Dulce Tentación','Luna Azul','Fragancia golosa de caramelo, vainilla y chocolate.','Gourmand','Mujer',50,45.0,72,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(10,'Sombra de Ébano','Raíz Noble','Perfume profundo con madera de ébano y especias.','Amaderado','Hombre',100,94.9000000000000056,15,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(11,'Luz de Primavera','Flor de Alba','Aroma ligero de flores silvestres y frutas frescas.','Floral','Mujer',100,39.9500000000000028,83,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(12,'Ámbar del Desierto','Alma Salvaje','Notas cálidas de ámbar, incienso y sándalo.','Oriental','Unisex',75,110.0,12,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(13,'Cielo de Verano','Costa Clara','Fragancia cítrica con mandarina, lima y neroli.','Cítrico','Unisex',100,42.5,91,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(14,'Rey de la Noche','Esencia Real','Aroma masculino con tabaco, cuero y vetiver.','Amaderado','Hombre',100,99.9500000000000028,24,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(15,'Susurro de Seda','Luna Azul','Perfume suave de almizcle, rosa y vainilla.','Floral','Mujer',50,68.0,38,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(16,'Montaña Salvaje','Raíz Noble','Notas verdes de romero, pino y tierra húmeda.','Verde','Hombre',100,57.8999999999999985,47,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(17,'Perla del Océano','Costa Clara','Fragancia marina con algas, sal y flores acuáticas.','Acuático','Mujer',75,51.9500000000000028,59,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(18,'Pasión Escarlata','Flor de Alba','Aroma sensual de frutos rojos, rosa y pachulí.','Frutal','Mujer',100,72.0,33,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(19,'Espíritu Libre','Alma Salvaje','Mezcla fresca de lavanda, salvia y bergamota.','Aromático','Unisex',100,64.5,52,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(20,'Oro de Oriente','Esencia Real','Perfume intenso de oud, azafrán y ámbar.','Oriental','Unisex',50,139.0,8,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(21,'Flor de Medianoche','Luna Azul','Notas nocturnas de jazmín, violeta y almizcle.','Floral','Mujer',75,81.5,27,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(22,'Viento del Norte','Raíz Noble','Fragancia fresca de eucalipto, menta y cedro.','Aromático','Hombre',100,53.8999999999999985,64,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(23,'Sol de Valencia','Costa Clara','Aroma mediterráneo de naranja, azahar y limón.','Cítrico','Unisex',100,44.9500000000000028,76,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(24,'Corazón de Rosa','Flor de Alba','Perfume romántico de rosa búlgara y frambuesa.','Floral','Mujer',50,61.0,48,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(25,'Tormenta Negra','Alma Salvaje','Fragancia poderosa de pimienta, incienso y cuero.','Especiado','Hombre',100,88.0,22,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(26,'Elegancia Eterna','Esencia Real','Notas refinadas de iris, sándalo y almizcle.','Amaderado','Unisex',75,119.950000000000002,17,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(27,'Luna de Plata','Luna Azul','Aroma delicado de pera, jazmín y vainilla.','Frutal','Mujer',100,58.5,56,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(28,'Sendero de Cedro','Raíz Noble','Perfume seco de cedro, vetiver y musgo.','Amaderado','Hombre',100,69.9000000000000056,39,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(29,'Agua de Coral','Costa Clara','Fragancia tropical con coco, lima y brisa marina.','Acuático','Unisex',75,49.9500000000000028,71,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(30,'Primavera Rosa','Flor de Alba','Notas suaves de peonía, melocotón y rosa.','Floral','Mujer',100,46.8999999999999985,85,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(31,'Instinto Salvaje','Alma Salvaje','Perfume masculino de cuero, tabaco y especias.','Oriental','Hombre',100,104.0,18,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(32,'Corona de Ámbar','Esencia Real','Aroma sofisticado de ámbar, vainilla y oud.','Oriental','Unisex',50,149.949999999999988,11,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(33,'Estrella Fugaz','Luna Azul','Fragancia luminosa de mandarina, flor de loto y almizcle.','Floral','Mujer',75,55.0,63,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(34,'Tierra Profunda','Raíz Noble','Notas terrosas de vetiver, pachulí y roble.','Amaderado','Hombre',100,76.5,34,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(35,'Costa del Sol','Costa Clara','Perfume veraniego de limón, coco y flores blancas.','Cítrico','Unisex',100,41.9500000000000028,92,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(36,'Beso de Primavera','Flor de Alba','Aroma dulce de cereza, peonía y vainilla.','Frutal','Mujer',50,52.8999999999999985,68,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(37,'Fuerza Ancestral','Alma Salvaje','Fragancia intensa de incienso, cuero y madera.','Especiado','Hombre',100,91.0,26,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(38,'Esencia de Diamante','Esencia Real','Perfume exclusivo de iris, rosa y ámbar gris.','Floral','Unisex',75,169.0,7,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(39,'Sueño de Vainilla','Luna Azul','Notas dulces de vainilla, almendra y caramelo.','Gourmand','Mujer',100,63.5,49,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(40,'Roble Centenario','Raíz Noble','Aroma robusto de roble, cedro y cuero.','Amaderado','Hombre',100,84.9500000000000028,31,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(41,'Isla Esmeralda','Costa Clara','Fragancia fresca de lima, menta y agua marina.','Acuático','Unisex',75,47.5,74,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(42,'Flor de Azahar','Flor de Alba','Perfume delicado de azahar, neroli y miel.','Floral','Mujer',100,56.9500000000000028,58,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(43,'Dragón de Fuego','Alma Salvaje','Aroma intenso de canela, pimienta y ámbar.','Especiado','Hombre',100,97.5,21,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(44,'Palacio de Oro','Esencia Real','Fragancia lujosa de rosa, oud y azafrán.','Oriental','Unisex',50,189.0,5,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(45,'Niebla de Luna','Luna Azul','Notas suaves de lavanda, violeta y almizcle.','Aromático','Mujer',75,66.9000000000000056,43,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(46,'Camino del Bosque','Raíz Noble','Perfume natural de pino, cedro y hojas verdes.','Verde','Unisex',100,59.0,62,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(47,'Mar de Cristal','Costa Clara','Aroma refrescante de sal marina, limón y jazmín.','Acuático','Unisex',100,54.5,69,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(48,'Dama de las Flores','Flor de Alba','Fragancia elegante de rosa, lirio y magnolia.','Floral','Mujer',75,78.9500000000000028,37,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(49,'Lobo Nocturno','Alma Salvaje','Perfume oscuro de cuero, pachulí y pimienta.','Amaderado','Hombre',100,112.0,14,'2026-11-19 16:46:12');
INSERT INTO productos VALUES(50,'Imperio de Plata','Esencia Real','Aroma exclusivo de sándalo, ámbar y almizcle.','Oriental','Unisex',100,159.949999999999988,9,'2026-11-19 16:46:12');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('productos',50);
COMMIT;
