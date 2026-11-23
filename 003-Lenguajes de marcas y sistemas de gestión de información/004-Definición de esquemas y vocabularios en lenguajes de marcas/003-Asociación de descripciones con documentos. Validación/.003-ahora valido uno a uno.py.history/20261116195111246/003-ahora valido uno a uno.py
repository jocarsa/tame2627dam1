import os																						# Importo libreria de sistema
from lxml import etree															# Importo libreria de XML

xsd = etree.XMLSchema(etree.parse("esquema.xsd"))		# Cargo la plantilla

carpeta = os.listdir("100curriculums")							# Inspecciono la carpeta

for archivo in carpeta:															# Para cada archivo en la carpeta
	xml = etree.parse("100curriculums/"+archivo)			# Carga  el archivo
  if xsd.validate(xml):															# Validalo
    print(archivo+": ok")														# Di ok
	else:
    print(archivo+": ko!!!!!!!!!!!!!!!!!!")					# o di ko
  