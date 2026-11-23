import os
from lxml import etree

xsd = etree.XMLSchema(etree.parse("esquema.xsd"))

carpeta = os.listdir("100curriculums")

for archivo in carpeta:
	xml = etree.parse("100curriculums/"+archivo)
  if xsd.validate(xml):
    print("XML válido")
	else:
    print("XML no válido")
    print(xsd.error_log)
  