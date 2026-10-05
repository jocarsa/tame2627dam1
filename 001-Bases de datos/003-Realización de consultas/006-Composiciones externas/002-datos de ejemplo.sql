-- ============================================
-- ALUMNOS
-- ============================================

INSERT INTO alumnos (nombre, apellidos, email) VALUES
('Ana', 'García López', 'ana.garcia@example.com'),
('Carlos', 'Martínez Ruiz', 'carlos.martinez@example.com'),
('Laura', 'Sánchez Pérez', 'laura.sanchez@example.com'),
('David', 'Fernández Gómez', 'david.fernandez@example.com'),
('Marta', 'López Navarro', 'marta.lopez@example.com'),
('Javier', 'Torres Molina', 'javier.torres@example.com'),
('Lucía', 'Ramírez Ortega', 'lucia.ramirez@example.com'),
('Pablo', 'Romero Vidal', 'pablo.romero@example.com'),
('Elena', 'Moreno Gil', 'elena.moreno@example.com'),
('Sergio', 'Jiménez Cano', 'sergio.jimenez@example.com'),
('Paula', 'Domínguez Serra', 'paula.dominguez@example.com'),
('Álvaro', 'Castro Ferrer', 'alvaro.castro@example.com'),
('Sara', 'Vega Pastor', 'sara.vega@example.com'),
('Daniel', 'Herrera Soler', 'daniel.herrera@example.com'),
('Cristina', 'Iglesias León', 'cristina.iglesias@example.com'),
('Miguel', 'Ramos Calvo', 'miguel.ramos@example.com'),
('Andrea', 'Santos Rubio', 'andrea.santos@example.com'),
('Rubén', 'Méndez Lozano', 'ruben.mendez@example.com'),
('Natalia', 'Fuentes Roca', 'natalia.fuentes@example.com'),
('Alejandro', 'Cortés Marín', 'alejandro.cortes@example.com'),
('Irene', 'Blasco Giménez', 'irene.blasco@example.com'),
('Víctor', 'Navarro Martí', 'victor.navarro@example.com'),
('Claudia', 'Pascual Ferrando', 'claudia.pascual@example.com'),
('Adrián', 'Gómez Sanz', 'adrian.gomez@example.com'),
('Beatriz', 'Ortiz Campos', 'beatriz.ortiz@example.com'),
('Hugo', 'Serrano Mora', 'hugo.serrano@example.com'),
('Silvia', 'Prieto Lara', 'silvia.prieto@example.com'),
('Mario', 'Requena Ibáñez', 'mario.requena@example.com'),
('Noelia', 'Caballero Esteve', 'noelia.caballero@example.com'),
('Raúl', 'Montero Beltrán', 'raul.montero@example.com');


-- ============================================
-- ASIGNATURAS
-- ============================================

INSERT INTO asignaturas (nombre, horas, codigo) VALUES
('Programación', 256, 'PROG'),
('Bases de Datos', 192, 'BBDD'),
('Lenguajes de Marcas', 128, 'LMSGI'),
('Entornos de Desarrollo', 96, 'ED'),
('Sistemas Informáticos', 192, 'SI'),
('Acceso a Datos', 120, 'AD'),
('Desarrollo de Interfaces', 120, 'DI'),
('Programación Multimedia', 100, 'PMDM'),
('Servicios y Procesos', 100, 'PSP'),
('Sistemas de Gestión Empresarial', 100, 'SGE');


-- ============================================
-- MATRÍCULAS
-- alumnos_id 1-30
-- asignaturas_id 1-10
-- ============================================

INSERT INTO matriculas (fecha, alumnos_id, asignaturas_id) VALUES

-- Ana
('2026-09-09', 1, 1),
('2026-09-09', 1, 2),
('2026-09-09', 1, 3),
('2026-09-09', 1, 4),
('2026-09-09', 1, 5),

-- Carlos
('2026-09-09', 2, 1),
('2026-09-09', 2, 2),
('2026-09-09', 2, 3),
('2026-09-09', 2, 4),
('2026-09-09', 2, 5),

-- Laura
('2026-09-10', 3, 1),
('2026-09-10', 3, 2),
('2026-09-10', 3, 3),
('2026-09-10', 3, 4),

-- David
('2026-09-10', 4, 1),
('2026-09-10', 4, 2),
('2026-09-10', 4, 4),
('2026-09-10', 4, 5),

-- Marta
('2026-09-10', 5, 1),
('2026-09-10', 5, 2),
('2026-09-10', 5, 3),
('2026-09-10', 5, 5),

-- Javier
('2026-09-11', 6, 1),
('2026-09-11', 6, 2),
('2026-09-11', 6, 3),

-- Lucía
('2026-09-11', 7, 1),
('2026-09-11', 7, 2),
('2026-09-11', 7, 4),
('2026-09-11', 7, 5),

-- Pablo
('2026-09-11', 8, 1),
('2026-09-11', 8, 3),
('2026-09-11', 8, 4),
('2026-09-11', 8, 5),

-- Elena
('2026-09-12', 9, 1),
('2026-09-12', 9, 2),
('2026-09-12', 9, 3),
('2026-09-12', 9, 4),
('2026-09-12', 9, 5),

-- Sergio
('2026-09-12', 10, 1),
('2026-09-12', 10, 2),
('2026-09-12', 10, 5),

-- Paula
('2026-09-13', 11, 1),
('2026-09-13', 11, 2),
('2026-09-13', 11, 3),
('2026-09-13', 11, 4),

-- Álvaro
('2026-09-13', 12, 1),
('2026-09-13', 12, 2),
('2026-09-13', 12, 3),
('2026-09-13', 12, 5),

-- Sara
('2026-09-14', 13, 1),
('2026-09-14', 13, 2),
('2026-09-14', 13, 4),

-- Daniel
('2026-09-14', 14, 1),
('2026-09-14', 14, 2),
('2026-09-14', 14, 3),
('2026-09-14', 14, 4),
('2026-09-14', 14, 5),

-- Cristina
('2026-09-14', 15, 1),
('2026-09-14', 15, 2),
('2026-09-14', 15, 3),

-- Miguel
('2026-09-15', 16, 6),
('2026-09-15', 16, 7),
('2026-09-15', 16, 8),
('2026-09-15', 16, 9),
('2026-09-15', 16, 10),

-- Andrea
('2026-09-15', 17, 6),
('2026-09-15', 17, 7),
('2026-09-15', 17, 8),
('2026-09-15', 17, 9),

-- Rubén
('2026-09-15', 18, 6),
('2026-09-15', 18, 7),
('2026-09-15', 18, 9),
('2026-09-15', 18, 10),

-- Natalia
('2026-09-16', 19, 6),
('2026-09-16', 19, 7),
('2026-09-16', 19, 8),
('2026-09-16', 19, 10),

-- Alejandro
('2026-09-16', 20, 6),
('2026-09-16', 20, 7),
('2026-09-16', 20, 8),
('2026-09-16', 20, 9),
('2026-09-16', 20, 10),

-- Irene
('2026-09-17', 21, 6),
('2026-09-17', 21, 7),
('2026-09-17', 21, 8),

-- Víctor
('2026-09-17', 22, 6),
('2026-09-17', 22, 8),
('2026-09-17', 22, 9),
('2026-09-17', 22, 10),

-- Claudia
('2026-09-17', 23, 6),
('2026-09-17', 23, 7),
('2026-09-17', 23, 9),

-- Adrián
('2026-09-18', 24, 6),
('2026-09-18', 24, 7),
('2026-09-18', 24, 8),
('2026-09-18', 24, 9),
('2026-09-18', 24, 10),

-- Beatriz
('2026-09-18', 25, 6),
('2026-09-18', 25, 7),
('2026-09-18', 25, 10),

-- Hugo
('2026-09-19', 26, 1),
('2026-09-19', 26, 2),
('2026-09-19', 26, 3),
('2026-09-19', 26, 4),

-- Silvia
('2026-09-19', 27, 1),
('2026-09-19', 27, 2),
('2026-09-19', 27, 3),
('2026-09-19', 27, 4),
('2026-09-19', 27, 5),

-- Mario
('2026-09-20', 28, 6),
('2026-09-20', 28, 7),
('2026-09-20', 28, 8),
('2026-09-20', 28, 9),

-- Noelia
('2026-09-20', 29, 6),
('2026-09-20', 29, 7),
('2026-09-20', 29, 8),
('2026-09-20', 29, 9),
('2026-09-20', 29, 10),

-- Raúl
('2026-09-21', 30, 6),
('2026-09-21', 30, 7),
('2026-09-21', 30, 9),
('2026-09-21', 30, 10);