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