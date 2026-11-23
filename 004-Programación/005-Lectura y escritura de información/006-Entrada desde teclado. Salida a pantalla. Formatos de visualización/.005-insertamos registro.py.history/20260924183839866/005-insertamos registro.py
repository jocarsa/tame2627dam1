'''
    Super programa agenda v0.3
    Jose Vicente Carratalá

    contacto
    - nombre
    - apellidos
    - email
    - telefono
'''

print("Programa agenda")
print("v0.3 Jose Vicente Carratala")
print("Gestiona tu propia agenda")

while True:
    print("Selecciona una opcion")
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
        archivo.close()

    elif opcion == "2":
        pass