import os
from lxml import etree

xsd = etree.XMLSchema(etree.parse("esquema.xsd"))

carpeta = os.listdir("100curriculums")

for archivo in carpeta:
	xml = etree.parse("100curriculums/"+archivo)
  if xsd.validate(xml):
    print(archivo+": ok")
	else:
    print(archivo+": ko!!!!!!!!!!!!!!!!!!")
  