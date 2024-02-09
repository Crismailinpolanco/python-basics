def contar_letra_en_frase(frase, letra):
    contador = 0
    for caracter in frase:
        if caracter.lower() == letra.lower():
            contador += 1
    return contador

# Solicitar la entrada al usuario
frase_usuario = input("Ingrese una frase: ")
letra_usuario = input("Ingrese una letra: ")

# Calcular el número de veces que aparece la letra en la frase
cantidad_apariciones = contar_letra_en_frase(frase_usuario, letra_usuario)

# Mostrar el resultado
print(f"La letra '{letra_usuario}' aparece {cantidad_apariciones} veces en la frase.")
