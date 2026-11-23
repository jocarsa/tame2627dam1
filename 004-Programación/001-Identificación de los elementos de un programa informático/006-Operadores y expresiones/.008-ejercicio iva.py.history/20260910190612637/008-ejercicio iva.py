# Muestre un mensaje indicando que va a calcular el precio final de un producto.
print("Voy a calcular el precio final de un producto")

# Pida al usuario que introduzca el precio del producto sin IVA.
base_imponible = input("Introduce el precio sin IVA")

# Pida al usuario que introduzca el porcentaje de IVA.
porcentaje_iva = input("Introduzca el porcentaje de IVA")

# Convierta los datos introducidos al tipo numérico adecuado.
base_numerica = float(base_imponible)
iva_numerico = int(porcentaje_iva)

# Calcule cuánto dinero corresponde al IVA.
total_iva = base_numerica*(iva_numerico/100)
                       
# Calcule el precio final del producto sumando el IVA.
total_producto = base_numerica + total_iva
                       
# Muestre en pantalla el precio original, el importe del IVA y el precio final.
print("El precio original es de",base_numerica)
print("el IVA es de",total_iva)
print("El precio final es de",total_producto)