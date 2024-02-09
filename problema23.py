def contar_frecuencia_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para evitar distinción entre mayúsculas y minúsculas
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def palabra_mas_repetida(diccionario):
    if not diccionario:
        return None, 0

    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    return palabra_max, frecuencia_max

# Ejemplo de uso:
cadena_input = "Escribir un programa en Python es un buen ejercicio. Python es un lenguaje versátil y poderoso."
diccionario_frecuencia = contar_frecuencia_palabras(cadena_input)
palabra_maxima, frecuencia_maxima = palabra_mas_repetida(diccionario_frecuencia)

# Mostrar resultados
print("Diccionario de frecuencias:", diccionario_frecuencia)
print("Palabra más repetida:", palabra_maxima)
print("Frecuencia de la palabra más repetida:", frecuencia_maxima)
