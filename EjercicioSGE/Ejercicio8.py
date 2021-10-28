asignatura = ['Matemática', 'Lengua', 'Historia', 'Física']
notaPuesta=0
notas=0

for nota in asignatura:
    print(nota)
    notaPuesta=int(input())
    notas=notas+notaPuesta
    print("Tu nota en {} es {}".format(nota, notaPuesta))
    print()

print("Tu media de notas es: {:.0f}".format(notas / asignatura.__len__()))