def determinar_grupo(nombre, sexo):
    # Convertir el nombre a minúsculas para comparar sin importar mayúsculas o minúsculas
    nombre_minusculas = nombre.lower()

    # Verificar el grupo según las condiciones dadas
    if (sexo == 'M' and nombre_minusculas < 'm') or (sexo == 'H' and nombre_minusculas >= 'n'):
        grupo = 'A'
    else:
        grupo = 'B'

    # Mostrar el resultado
    print(f"El alumno pertenece al grupo {grupo}.")

# Ejemplo de uso:
nombre_alumno = input("Introduce tu nombre: ")
sexo_alumno = input("Introduce tu sexo (M/F): ").upper()

determinar_grupo(nombre_alumno, sexo_alumno)
