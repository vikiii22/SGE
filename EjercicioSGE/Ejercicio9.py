asignatura = ['Matemáticas', 'Lengua', 'Historia', 'Física']
notas = []

print("Añade tus notas en cada asignatura:")
for a in asignatura:
    print(a)
    notaPuesta = int(input())
    notas.append(notaPuesta)

recuperar=[]
aprobadas=[]
for l in range(len(asignatura)):
    print(notas[l], " " + asignatura[l])
    if notas[l] < 5:
        recuperar.append(asignatura[l])
    else:
        aprobadas.append(asignatura[l])

for apro in aprobadas:
    asignatura.remove(apro)

print("Tienes que recuperar: " + str(asignatura))