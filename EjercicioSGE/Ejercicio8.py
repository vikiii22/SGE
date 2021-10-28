asignatura = ['Matemática', 'Lengua', 'Historia', 'Física']
notas=[]
notasMedia=0
print("Añade tus notas en cada asignatura:")
for a in asignatura:
    print(a)
    notaPuesta=int(input())
    notas.append(notaPuesta)

for l in range(len(asignatura)):
    print("Tu nota en {} es {}".format(asignatura[l], notas[l]))
    notasMedia=notasMedia+notas[l]

print("---------MEDIA---------")
print("Tu media de notas es: {:.0f}".format(notasMedia / len(asignatura)))