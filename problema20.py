# Diccionario con los créditos de las asignaturas
creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# Mostrar los créditos de cada asignatura
for asignatura, creditos in creditos_asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos.")

# Calcular el número total de créditos del curso
total_creditos = sum(creditos_asignaturas.values())

# Mostrar el número total de créditos del curso
print(f"\nNúmero total de créditos del curso: {total_creditos}")
