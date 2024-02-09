def mostrar_letras_invertidas(palabra):
    for letra in palabra[::-1]:
        print(letra)

# Solicitar la entrada al usuario
palabra_usuario = input("Ingrese una palabra: ")

# Mostrar las letras de la palabra de atrás hacia adelante
mostrar_letras_invertidas(palabra_usuario)
