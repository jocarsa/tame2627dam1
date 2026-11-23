# Muestre un mensaje indicando que va a calcular el precio final de un producto.
print("Voy a calcular el precio final de un producto")

# Pida al usuario que introduzca el precio del producto sin IVA.
base_imponible = input("Introduce el precio sin IVA")

# Pida al usuario que introduzca el porcentaje de IVA.
porcentaje_iva = input("Introduzca el porcentaje de IVA)

# Convierta los datos introducidos al tipo numérico adecuado.
base_numerica = float(base_imponible)
iva_numerico = int(porcentaje_iva)

# Calcule cuánto dinero corresponde al IVA.
total_iva = base_numerica*(iva_numerico/100)
                       
# Calcule el precio final del producto sumando el IVA.
# Muestre en pantalla el precio original, el importe del IVA y el precio final.

