def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total

# Ejemplos de uso:

# Caso 1: Se proporciona el porcentaje de IVA
cantidad_sin_iva1 = 100
porcentaje_iva1 = 10
total_factura1 = calcular_total_factura(cantidad_sin_iva1, porcentaje_iva1)
print(f"Total con {porcentaje_iva1}% de IVA: {total_factura1} €")

# Caso 2: No se proporciona el porcentaje de IVA (utiliza el valor por defecto 21%)
cantidad_sin_iva2 = 200
total_factura2 = calcular_total_factura(cantidad_sin_iva2)
print(f"Total con 21% de IVA (por defecto): {total_factura2} €")
