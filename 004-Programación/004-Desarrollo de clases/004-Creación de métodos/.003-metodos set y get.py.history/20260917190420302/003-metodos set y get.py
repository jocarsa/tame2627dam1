class Gato():
  def __init__(self):
    self.edad = 0				# Propiedad
    self.color = ""			# Propiedad
  def maullar(self):
    print("El gato está maullando") # Método
  def arañar(self):
    print("El gato te araña")
  def getColor(self):
    return self.color
  def setColor(self,nuevocolor):
    self.color = nuevocolor

micifu = Gato()
micifu.setColor("naranja")
    
