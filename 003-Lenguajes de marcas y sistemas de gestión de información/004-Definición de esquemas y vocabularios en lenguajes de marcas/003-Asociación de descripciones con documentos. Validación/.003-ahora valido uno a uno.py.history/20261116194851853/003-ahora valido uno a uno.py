import os
from lxml import etree

xsd = etree.XMLSchema(etree.parse("esquema.xsd"))

carpeta = os.listdir("100curriculums")

for archivo in carpeta:
    