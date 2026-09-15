try:
  edad = 18
  assert edad < 30
except Exception as e:
  print("No puedo ejecutar porque no quiero")
  print(e)

print("Y continuamos el programa")