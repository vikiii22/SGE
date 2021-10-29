asignaturas = {'SGE': 6, 'Programación': 4, 'Desarrollo de Interfaces': 5}
creditos = 0
for i in asignaturas.keys():
    print(i, "Tiene", asignaturas.get(i), "créditos")
    creditos = creditos + asignaturas.get(i)

print("Los créditos totales del curso son:", creditos)
