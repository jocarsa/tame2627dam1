'''
    Super programa agenda v0.4
    Jose Vicente Carratalá

    contacto
    - nombre
    - apellidos
    - email
    - telefono
'''

print("Programa agenda")
print("v0.4 Jose Vicente Carratala")
print("Gestiona tu propia agenda")

while True:
    print("\nSelecciona una opcion")
    print("1.-Insertar un registro")
    print("2.-Listar registros")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Dime el nombre del nuevo registro: ")
        apellidos = input("Dime los apellidos del nuevo registro: ")
        email = input("Dime el email del nuevo registro: ")
        telefono = input("Dime el telefono del nuevo registro: ")

        archivo = open("agenda.csv", "a")
        archivo.write(nombre + "|" + apellidos + "|" + email + "|" + telefono + "\n")
        archivo.close()

        print("Tu archivo ha sido guardado")

    elif opcion == "2":

        archivo = open("agenda.csv", "r")

        # Leo la primera línea, que contiene las cabeceras
        cabecera = archivo.readline()

        # Separo las cabeceras
        cabeceras = cabecera.strip().split("|")

        # Leo el resto de líneas
        lineas = archivo.readlines()

        # Recorro todos los registros
        for linea in lineas:

            # Separo los campos del registro
            datos = linea.strip().split("|")

            print("------------------------------")

            # Muestro cabecera : valor
            for i in range(0, len(datos)):
                print(cabeceras[i], ":", datos[i])

        print("------------------------------")

        archivo.close()