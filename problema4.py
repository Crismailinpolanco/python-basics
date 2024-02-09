def extraer_numero_telefono(numero_telefono):
    # Separar el número en prefijo, número y extensión
    partes = numero_telefono.split('-')

    # Extraer el número sin prefijo y extensión
    numero_sin_prefijo_ext = partes[1]

    # Mostrar el resultado
    print("Número sin prefijo y extensión:", numero_sin_prefijo_ext)

# Ejemplo de uso:
telefono_empresa = "+34-913724710-56"
extraer_numero_telefono(telefono_empresa)
