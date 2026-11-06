# JOCARSA · Blog personal

Proyecto Flask + MySQL con front editorial y administración renovada.

## Instalación

```bash
pip install flask mysql-connector-python
export DB_HOST=localhost
export DB_USER=blogdamtame2627
export DB_PASSWORD='TU_PASSWORD'
export DB_NAME=blogdamtame2627
export FLASK_SECRET_KEY='una-clave-aleatoria-segura'
python3 001-miniflask.py
```

La tabla `articulos` debe existir con columnas `id`, `titulo`, `fecha`, `contenido`.

Rutas: `/` blog, `/articulos` JSON, `/listado` administración, `/nuevo` formulario, `/inserta` POST.

**Importante:** el panel de administración no incluye autenticación, igual que el proyecto de origen. Añade autenticación y CSRF antes de exponerlo a Internet.
