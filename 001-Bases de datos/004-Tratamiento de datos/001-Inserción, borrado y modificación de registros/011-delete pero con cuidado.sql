DELETE FROM alumnos
WHERE id = 23;

SELECT * FROM alumnos;

DELETE FROM alumnos
WHERE nombre = 'David';

INSERT INTO alumnos 
(id,nombre,apellidos,email)
VALUES 
(NULL,'Jose Vicente','Carratalá Sanchis','info@jocarsa.com');