def imprimir_triangulo_rectangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)

# Solicitar la entrada al usuario
try:
    altura_triangulo = int(input("Ingrese la altura del triángulo rectángulo: "))
    imprimir_triangulo_rectangulo(altura_triangulo)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
