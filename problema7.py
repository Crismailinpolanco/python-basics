def verificar_contrasena(contrasena_guardada, contrasena_introducida):
    if contrasena_guardada.lower() == contrasena_introducida.lower():
        print("¡Contraseña correcta!")
    else:
        print("Contraseña incorrecta.")

# Ejemplo de uso:
contrasena_guardada = "MiContrasenaSegura"
contrasena_usuario = input("Introduce tu contraseña: ")

verificar_contrasena(contrasena_guardada, contrasena_usuario)
