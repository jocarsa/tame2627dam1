
from lxml import etree

xml = etree.parse("curriculum.xml")
xsd = etree.XMLSchema(etree.parse("curriculum.xsd"))

if xsd.validate(xml):
    print("XML válido")
else:
    print("XML no válido")
    print(xsd.error_log)
