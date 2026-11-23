class Mamifero():
  def __init__(self):
    self.edad = 0
    self.color = ""
  def mamar(self):
    print("Este animal está mamando")

class Gato(Mamifero):
  def __init__(self):
    self.super()

class Perro(Mamifero):
  def __init__(self):
    self.super()

micifu = Gato()