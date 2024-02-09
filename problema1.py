def imprimir_nombre(nombre_usuario, numero_veces):
    for _ in range(numero_veces):
        print(nombre_usuario)

# Ejemplo de uso:
nombre = input("Introduce tu nombre: ")
veces = int(input("Introduce un número entero: "))

imprimir_nombre(nombre, veces)