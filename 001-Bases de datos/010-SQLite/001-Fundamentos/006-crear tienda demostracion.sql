DROP TABLE IF EXISTS productos;

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

INSERT INTO productos
(nombre, marca, descripcion, categoria, genero, capacidad_ml, precio, stock)
VALUES
('Amanecer Dorado', 'Esencia Real', 'Fragancia fresca con notas de bergamota, jazmín y almizcle.', 'Floral', 'Mujer', 100, 59.95, 45),
('Noche de Cristal', 'Luna Azul', 'Perfume elegante con vainilla, ámbar y flores blancas.', 'Oriental', 'Mujer', 75, 74.50, 32),
('Bosque Encantado', 'Raíz Noble', 'Aroma amaderado con cedro, pino y musgo.', 'Amaderado', 'Hombre', 100, 65.00, 28),
('Brisa Mediterránea', 'Costa Clara', 'Fragancia marina con limón, sal y lavanda.', 'Acuático', 'Unisex', 100, 48.90, 67),
('Rosa Imperial', 'Esencia Real', 'Perfume floral de rosas, peonías y almizcle blanco.', 'Floral', 'Mujer', 50, 89.00, 19),
('Fuego Interior', 'Alma Salvaje', 'Aroma intenso de pimienta negra, cuero y madera.', 'Especiado', 'Hombre', 100, 79.95, 36),
('Jardín Secreto', 'Flor de Alba', 'Mezcla delicada de gardenia, jazmín y magnolia.', 'Floral', 'Mujer', 75, 54.90, 54),
('Horizonte Azul', 'Costa Clara', 'Notas frescas de océano, menta y cítricos.', 'Acuático', 'Hombre', 100, 62.50, 41),
('Dulce Tentación', 'Luna Azul', 'Fragancia golosa de caramelo, vainilla y chocolate.', 'Gourmand', 'Mujer', 50, 45.00, 72),
('Sombra de Ébano', 'Raíz Noble', 'Perfume profundo con madera de ébano y especias.', 'Amaderado', 'Hombre', 100, 94.90, 15),

('Luz de Primavera', 'Flor de Alba', 'Aroma ligero de flores silvestres y frutas frescas.', 'Floral', 'Mujer', 100, 39.95, 83),
('Ámbar del Desierto', 'Alma Salvaje', 'Notas cálidas de ámbar, incienso y sándalo.', 'Oriental', 'Unisex', 75, 110.00, 12),
('Cielo de Verano', 'Costa Clara', 'Fragancia cítrica con mandarina, lima y neroli.', 'Cítrico', 'Unisex', 100, 42.50, 91),
('Rey de la Noche', 'Esencia Real', 'Aroma masculino con tabaco, cuero y vetiver.', 'Amaderado', 'Hombre', 100, 99.95, 24),
('Susurro de Seda', 'Luna Azul', 'Perfume suave de almizcle, rosa y vainilla.', 'Floral', 'Mujer', 50, 68.00, 38),
('Montaña Salvaje', 'Raíz Noble', 'Notas verdes de romero, pino y tierra húmeda.', 'Verde', 'Hombre', 100, 57.90, 47),
('Perla del Océano', 'Costa Clara', 'Fragancia marina con algas, sal y flores acuáticas.', 'Acuático', 'Mujer', 75, 51.95, 59),
('Pasión Escarlata', 'Flor de Alba', 'Aroma sensual de frutos rojos, rosa y pachulí.', 'Frutal', 'Mujer', 100, 72.00, 33),
('Espíritu Libre', 'Alma Salvaje', 'Mezcla fresca de lavanda, salvia y bergamota.', 'Aromático', 'Unisex', 100, 64.50, 52),
('Oro de Oriente', 'Esencia Real', 'Perfume intenso de oud, azafrán y ámbar.', 'Oriental', 'Unisex', 50, 139.00, 8),

('Flor de Medianoche', 'Luna Azul', 'Notas nocturnas de jazmín, violeta y almizcle.', 'Floral', 'Mujer', 75, 81.50, 27),
('Viento del Norte', 'Raíz Noble', 'Fragancia fresca de eucalipto, menta y cedro.', 'Aromático', 'Hombre', 100, 53.90, 64),
('Sol de Valencia', 'Costa Clara', 'Aroma mediterráneo de naranja, azahar y limón.', 'Cítrico', 'Unisex', 100, 44.95, 76),
('Corazón de Rosa', 'Flor de Alba', 'Perfume romántico de rosa búlgara y frambuesa.', 'Floral', 'Mujer', 50, 61.00, 48),
('Tormenta Negra', 'Alma Salvaje', 'Fragancia poderosa de pimienta, incienso y cuero.', 'Especiado', 'Hombre', 100, 88.00, 22),
('Elegancia Eterna', 'Esencia Real', 'Notas refinadas de iris, sándalo y almizcle.', 'Amaderado', 'Unisex', 75, 119.95, 17),
('Luna de Plata', 'Luna Azul', 'Aroma delicado de pera, jazmín y vainilla.', 'Frutal', 'Mujer', 100, 58.50, 56),
('Sendero de Cedro', 'Raíz Noble', 'Perfume seco de cedro, vetiver y musgo.', 'Amaderado', 'Hombre', 100, 69.90, 39),
('Agua de Coral', 'Costa Clara', 'Fragancia tropical con coco, lima y brisa marina.', 'Acuático', 'Unisex', 75, 49.95, 71),
('Primavera Rosa', 'Flor de Alba', 'Notas suaves de peonía, melocotón y rosa.', 'Floral', 'Mujer', 100, 46.90, 85),

('Instinto Salvaje', 'Alma Salvaje', 'Perfume masculino de cuero, tabaco y especias.', 'Oriental', 'Hombre', 100, 104.00, 18),
('Corona de Ámbar', 'Esencia Real', 'Aroma sofisticado de ámbar, vainilla y oud.', 'Oriental', 'Unisex', 50, 149.95, 11),
('Estrella Fugaz', 'Luna Azul', 'Fragancia luminosa de mandarina, flor de loto y almizcle.', 'Floral', 'Mujer', 75, 55.00, 63),
('Tierra Profunda', 'Raíz Noble', 'Notas terrosas de vetiver, pachulí y roble.', 'Amaderado', 'Hombre', 100, 76.50, 34),
('Costa del Sol', 'Costa Clara', 'Perfume veraniego de limón, coco y flores blancas.', 'Cítrico', 'Unisex', 100, 41.95, 92),
('Beso de Primavera', 'Flor de Alba', 'Aroma dulce de cereza, peonía y vainilla.', 'Frutal', 'Mujer', 50, 52.90, 68),
('Fuerza Ancestral', 'Alma Salvaje', 'Fragancia intensa de incienso, cuero y madera.', 'Especiado', 'Hombre', 100, 91.00, 26),
('Esencia de Diamante', 'Esencia Real', 'Perfume exclusivo de iris, rosa y ámbar gris.', 'Floral', 'Unisex', 75, 169.00, 7),
('Sueño de Vainilla', 'Luna Azul', 'Notas dulces de vainilla, almendra y caramelo.', 'Gourmand', 'Mujer', 100, 63.50, 49),
('Roble Centenario', 'Raíz Noble', 'Aroma robusto de roble, cedro y cuero.', 'Amaderado', 'Hombre', 100, 84.95, 31),

('Isla Esmeralda', 'Costa Clara', 'Fragancia fresca de lima, menta y agua marina.', 'Acuático', 'Unisex', 75, 47.50, 74),
('Flor de Azahar', 'Flor de Alba', 'Perfume delicado de azahar, neroli y miel.', 'Floral', 'Mujer', 100, 56.95, 58),
('Dragón de Fuego', 'Alma Salvaje', 'Aroma intenso de canela, pimienta y ámbar.', 'Especiado', 'Hombre', 100, 97.50, 21),
('Palacio de Oro', 'Esencia Real', 'Fragancia lujosa de rosa, oud y azafrán.', 'Oriental', 'Unisex', 50, 189.00, 5),
('Niebla de Luna', 'Luna Azul', 'Notas suaves de lavanda, violeta y almizcle.', 'Aromático', 'Mujer', 75, 66.90, 43),
('Camino del Bosque', 'Raíz Noble', 'Perfume natural de pino, cedro y hojas verdes.', 'Verde', 'Unisex', 100, 59.00, 62),
('Mar de Cristal', 'Costa Clara', 'Aroma refrescante de sal marina, limón y jazmín.', 'Acuático', 'Unisex', 100, 54.50, 69),
('Dama de las Flores', 'Flor de Alba', 'Fragancia elegante de rosa, lirio y magnolia.', 'Floral', 'Mujer', 75, 78.95, 37),
('Lobo Nocturno', 'Alma Salvaje', 'Perfume oscuro de cuero, pachulí y pimienta.', 'Amaderado', 'Hombre', 100, 112.00, 14),
('Imperio de Plata', 'Esencia Real', 'Aroma exclusivo de sándalo, ámbar y almizcle.', 'Oriental', 'Unisex', 100, 159.95, 9);