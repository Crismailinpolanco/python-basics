def imprimir_triangulo_invertido(altura):
    for i in range(1, altura * 2, 2):
        for j in range(i, 0, -2):
            print(j, end=' ')
        print()

# Solicitar la entrada al usuario
try:
    altura_triangulo = int(input("Ingrese la altura del triángulo invertido: "))
    imprimir_triangulo_invertido(altura_triangulo)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
