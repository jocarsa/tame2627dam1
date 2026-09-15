dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

try:
  division = dividendo/divisor
  print(division)
except Exception as e:
  print("Ha ocurrido un error pero continuamos:", e)

print("Pero es que yo quiero que mi programa siga funcionando")