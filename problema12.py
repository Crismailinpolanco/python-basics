def menu_pizza():
    print("Bienvenido a Bella Napoli, la mejor pizzería del mundo!")
    print("¿Qué tipo de pizza te gustaría ordenar?")
    print("1. Pizza vegetariana")
    print("2. Pizza no vegetariana")

    # Solicitar la elección al usuario
    eleccion_tipo_pizza = input("Ingresa 1 para pizza vegetariana o 2 para pizza no vegetariana: ")

    if eleccion_tipo_pizza == "1":
        tipo_pizza = "Vegetariana"
        ingredientes_disponibles = ["mozzarella", "tomate", "pimiento", "tofu"]
    elif eleccion_tipo_pizza == "2":
        tipo_pizza = "No Vegetariana"
        ingredientes_disponibles = ["mozzarella", "tomate", "peperoni", "jamón", "salmón"]
    else:
        print("Elección no válida. Por favor, selecciona 1 o 2.")
        return

    print(f"\nExcelente elección. Tu pizza {tipo_pizza} puede incluir uno de los siguientes ingredientes:")

    # Mostrar ingredientes disponibles
    for i, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"{i}. {ingrediente}")

    # Solicitar la elección del ingrediente al usuario
    try:
        eleccion_ingrediente = int(input("Ingresa el número del ingrediente que deseas añadir: "))
        if 1 <= eleccion_ingrediente <= len(ingredientes_disponibles):
            ingrediente_elegido = ingredientes_disponibles[eleccion_ingrediente - 1]
            print(f"\n¡Excelente elección! Tu pizza {tipo_pizza} llevará {ingrediente_elegido}, mozzarella y tomate.")
        else:
            print("Elección no válida. Por favor, selecciona un número válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Ejecutar la función del menú de pizza
menu_pizza()
