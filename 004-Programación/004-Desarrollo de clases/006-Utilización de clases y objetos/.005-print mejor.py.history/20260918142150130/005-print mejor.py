class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
clientes = []

print("vamos a insertar clientes:")
while True:
  print("Introducimos  un nuevo cliente")
  nombre = input("Dime su nombre: ")
  apellidos = input("Dime sus apellidos: ")
  email = input("Dime su email: ")
  clientes.append(Cliente(nombre,apellidos,email))
  print("-"*30)
  for cliente in clientes:
    print(cliente.*)
    print("-"*20)
  print("-"*30)