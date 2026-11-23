class Gato():
  def __init__(self):
    self.edad = 0				# Propiedad
    self.color = ""			# Propiedad
  def maullar(self):
    print("El gato está maullando") # Método
  def arañar(self):
    print("El gato te araña")
    
micifu = Gato()
micifu.maullar()