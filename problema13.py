def calcular_capital_inversion(cantidad_invertir, tasa_interes_anual, num_anios):
    capital = cantidad_invertir

    for anio in range(1, num_anios + 1):
        capital *= 1 + tasa_interes_anual / 100
        print(f"Año {anio}: Capital obtenido = {capital:.2f} €")

# Solicitar la entrada al usuario
try:
    cantidad_invertir = float(input("Ingrese la cantidad a invertir (en euros): "))
    tasa_interes_anual = float(input("Ingrese el interés anual (en porcentaje): "))
    num_anios = int(input("Ingrese el número de años de la inversión: "))

    calcular_capital_inversion(cantidad_invertir, tasa_interes_anual, num_anios)
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
