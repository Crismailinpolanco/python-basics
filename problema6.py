def verificar_mayor_edad(edad):
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")

# Ejemplo de uso:
edad_usuario = int(input("Introduce tu edad: "))
verificar_mayor_edad(edad_usuario)
