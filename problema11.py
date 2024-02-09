def calcular_precio_entrada(edad):
    if edad < 4:
        precio = 0
    elif 4 <= edad <= 18:
        precio = 5
    else:
        precio = 10
    return precio

# Solicitar la edad al usuario
try:
    edad_cliente = int(input("Ingrese la edad del cliente: "))
    precio_entrada = calcular_precio_entrada(edad_cliente)

    if precio_entrada == 0:
        print("El cliente puede entrar gratis.")
    else:
        print(f"El precio de la entrada es: {precio_entrada}€")
except ValueError:
    print("Por favor, ingrese una edad válida (número entero).")
