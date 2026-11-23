#!/usr/bin/env python3

import datetime
import os
import subprocess

# Obtenemos fecha y hora actuales
current_datetime = datetime.datetime.now()

# La convertimos en un nombre válido para una carpeta
fecha = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

# Carpeta donde guardaremos todos los backups
carpeta_backups = "/home/josevicente/cron/backups"

# Carpeta específica de este backup
carpeta_actual = carpeta_backups + "/" + fecha

# Creamos la carpeta
os.makedirs(carpeta_actual, exist_ok=True)

# Archivo SQL que vamos a generar
archivo_sql = carpeta_actual + "/dam1.sql"

# Ejecutamos mysqldump
comando = [
    "/usr/bin/mysqldump",
    "--no-tablespaces",
    "-u", "backup",
    "-pTame123$$$",
    "dam1"
]

# Guardamos la salida de mysqldump en dam1.sql
with open(archivo_sql, "w") as archivo:
    subprocess.run(
        comando,
        stdout=archivo
    )

print("Backup realizado correctamente")
print("Carpeta:", carpeta_actual)
print("Archivo:", archivo_sql)