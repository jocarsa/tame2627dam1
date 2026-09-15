dividendo = int(input("Introduce el dividendo: "))

try:
  division = 10/0
  print(division)
except Exception as e:
  print("Ha ocurrido un error pero continuamos:", e)

print("Pero es que yo quiero que mi programa siga funcionando")