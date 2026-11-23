SELECT 

matriculas.fecha,
matriculas.alumnos_id,
matriculas.asignaturas_id,

alumnos.nombre,
alumnos.apellidos,
alumnos.email

FROM matriculas

LEFT JOIN alumnos ON matriculas.alumnos_id = alumnos.id
LEFT JOIN asignaturas ON matriculas.asignaturas_id = asignaturas.id
;