import os																						# Importo libreria de sistema
from lxml import etree															# Importo libreria de XML

xsd = etree.XMLSchema(etree.parse("esquema.xsd"))		# Cargo la plantilla

carpeta = os.listdir("100curriculums")

for archivo in carpeta:
	xml = etree.parse("100curriculums/"+archivo)
  if xsd.validate(xml):
    print(archivo+": ok")
	else:
    print(archivo+": ko!!!!!!!!!!!!!!!!!!")
  