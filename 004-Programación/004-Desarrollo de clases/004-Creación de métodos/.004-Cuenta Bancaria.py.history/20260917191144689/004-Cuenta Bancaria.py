class CuentaBancaria():
  def __init__(self):
    self.saldo = 0
  def retirarSaldo(self,cantidad):
    if cantidad < 10000:
      if cantidad < self.saldo:
    		self.saldo = self.saldo - cantidad
      else:
        print("Saldo insuficiente para esa operacion")
  def ponerSaldo(self,cantidad):
    if cantidad > 10000:
      print("Avisando a la entidad")
    self.saldo = cantidad
      
      
Micuenta = CuentaBancaria()
Micuenta.ponerSaldo(400)
      