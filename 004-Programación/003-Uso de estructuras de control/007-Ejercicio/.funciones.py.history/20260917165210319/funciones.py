def muestraMensajeBienvenida():
  print("Programa agenda en funciones:")
  print("v0.1 Jose Vicente Carratala")
  print("-"*30)

def muestraMenu():
  print("-"*30)
  print("Escoge una opción:")
  print("1.-Leer registros")
  print("2.-Insertar registros")
  print("3.-Actualizar registros")
  print("4.-Eliminar registros")
  
def listarRegistros(clientes):
  print("Vamos a listar los clientes")
  print(clientes)

def crearRegistro(clientes,registro):
  clientes.append(registro)
  return clientes

def actualizarRegistro():
  pass

def eliminarRegistro():
  pass