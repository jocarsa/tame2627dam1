class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
  def ponDatos(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
  def dameDatos(self):
    return [self.nombre,self.apellidos,self.email]
  
clientes = []

print("Agenda de clientes v0.1")
while True:
  print("Selecciona una opción")
  print("1.-Introducir un nuevo cliente")
  print("2.-Lista de clientes")
  opcion = input("Seleciona una opcion: ")
  if opcion == "1":
    nombre = input("Dime el nombre del nuevo cliente: ")
    apellidos = input("Dime los apellidos del nuevo cliente: ")
    email = input("Dime el email del nuevo cliente: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == "2":
    for cliente in clientes:
      print(cliente.dameDatos())