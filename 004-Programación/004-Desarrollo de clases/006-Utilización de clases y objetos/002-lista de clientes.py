class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
clientes = []

clientes.append(Cliente("JV","C","info@jocarsa.com"))
clientes.append(Cliente("Sergio","Martinez","sergio@jocarsa.com"))

print(clientes)