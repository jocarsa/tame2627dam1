from lxml import etree

# Cargar el esquema XSD
archivo_xsd = etree.parse("plantilla validacion.xsd")
esquema = etree.XMLSchema(archivo_xsd)

# Cargar el XML
archivo_xml = etree.parse("001-plantilla cliente.xml")

# Validar
if esquema.validate(archivo_xml):
    print("El XML es válido")
else:
    print("El XML NO es válido")

    # Mostrar los errores
    for error in esquema.error_log:
        print("Línea:", error.line)
        print("Error:", error.message)