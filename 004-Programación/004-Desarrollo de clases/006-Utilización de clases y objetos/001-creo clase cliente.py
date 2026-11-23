class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
cliente1 = Cliente(
  "Jose Vicente",
  "Carratala",
  "info@jocarsa.com"
)

cliente2 = Cliente(
  "Jaime",
  "Martinez",
  "jaime@jocarsa.com"
)

print(cliente1)
print(cliente2)





