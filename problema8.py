def verificar_tributacion():
    # Solicitar la edad y los ingresos mensuales al usuario
    edad = int(input("Introduce tu edad: "))
    ingresos_mensuales = float(input("Introduce tus ingresos mensuales (en euros): "))

    # Verificar si cumple con las condiciones para tributar
    if edad > 16 and ingresos_mensuales >= 1000:
        print("Debes tributar.")
    else:
        print("No tienes que tributar.")

# Ejecutar la función para verificar la tributación
verificar_tributacion()
