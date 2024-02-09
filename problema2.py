def mostrar_nombre_variaciones(nombre_completo):
    # Mostrar el nombre completo en minúsculas
    print("Nombre en minúsculas:", nombre_completo.lower())

    # Mostrar el nombre completo en mayúsculas
    print("Nombre en mayúsculas:", nombre_completo.upper())

    # Dividir el nombre completo en palabras y capitalizar la primera letra de cada palabra
    palabras = nombre_completo.split()
    nombre_formateado = ' '.join([palabra.capitalize() for palabra in palabras])
    print("Nombre con la primera letra en mayúscula:", nombre_formateado)

# Ejemplo de uso:
nombre_usuario = input("Introduce tu nombre completo: ")
mostrar_nombre_variaciones(nombre_usuario)
