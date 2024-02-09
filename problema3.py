def mostrar_informacion_nombre(nombre_usuario):
    nombre_mayusculas = nombre_usuario.upper()
    cantidad_letras = len(nombre_usuario)

    mensaje = f"{nombre_mayusculas} tiene {cantidad_letras} letras."
    print(mensaje)

# Ejemplo de uso:
nombre = input("Introduce tu nombre: ")
mostrar_informacion_nombre(nombre)
