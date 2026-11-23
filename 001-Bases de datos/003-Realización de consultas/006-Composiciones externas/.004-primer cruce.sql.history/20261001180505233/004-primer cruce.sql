SELECT 

matriculas.fecha,
matriculas.alumnos_id,
matriculas.asignaturas_id

FROM matriculas

LEFT JOIN alumnos ON matriculas.alumnos_id = alumnos.id
;