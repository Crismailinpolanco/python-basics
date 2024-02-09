def ingresar_notas(asignaturas):
    notas = []
    for asignatura in asignaturas:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        notas.append(nota)
    return notas

def mostrar_notas(asignaturas, notas):
    for i in range(len(asignaturas)):
        print(f"En {asignaturas[i]} has sacado {notas[i]}")

# Lista de asignaturas
asignaturas_del_curso = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Ingresar notas
notas_obtenidas = ingresar_notas(asignaturas_del_curso)

# Mostrar las notas por pantalla
mostrar_notas(asignaturas_del_curso, notas_obtenidas)
