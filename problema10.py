def calcular_beneficios(puntuacion):
    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
    else:
        nivel = "Valor no válido"

    if nivel != "Valor no válido":
        beneficios = 2400 * puntuacion
        print(f"Nivel de rendimiento: {nivel}")
        print(f"Cantidad de dinero recibida: {beneficios}€")
    else:
        print("La puntuación ingresada no es válida.")

# Solicitar la puntuación al usuario
try:
    puntuacion_usuario = float(input("Ingrese su puntuación (0.0, 0.4, 0.6 o más): "))
    calcular_beneficios(puntuacion_usuario)
except ValueError:
    print("Por favor, ingrese un valor numérico válido.")
