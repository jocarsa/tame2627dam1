SELECT 

matriculas.fecha,

alumnos.nombre,
alumnos.apellidos,

asignaturas.nombre

FROM matriculas

LEFT JOIN alumnos ON matriculas.alumnos_id = alumnos.id
LEFT JOIN asignaturas ON matriculas.asignaturas_id = asignaturas.id
;