class Animal():
  def __init__(self):
    self.edad = 0
    self.color = ""

class Mamifero():
  def __init__(self):
    super().__init__()
  def mamar(self):
    print("Este animal está mamando")

class Gato(Mamifero):
  def __init__(self):
    super().__init__()

class Perro(Mamifero):
  def __init__(self):
    super().__init__()

class Tortuga(Animal):

micifu = Gato()
micifu.mamar()