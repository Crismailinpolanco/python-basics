def eliminar_aprobadas(asignaturas, notas):
    asignaturas_repetir = []
    for i in range(len(asignaturas)):
        if notas[i] < 5.0:
            asignaturas_repetir.append(asignaturas[i])
    return asignaturas_repetir

# Lista de asignaturas
asignaturas_del_curso = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Ingresar notas
notas_obtenidas = []
for asignatura in asignaturas_del_curso:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    notas_obtenidas.append(nota)

# Eliminar asignaturas aprobadas
asignaturas_repetir = eliminar_aprobadas(asignaturas_del_curso, notas_obtenidas)

# Mostrar las asignaturas a repetir
if len(asignaturas_repetir) > 0:
    print("Debes repetir las siguientes asignaturas:")
    for asignatura in asignaturas_repetir:
        print(asignatura)
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
