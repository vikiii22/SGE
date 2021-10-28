frase=input("Introduce una frase: ")
letra=input("Introduce la letra: ")
vecesAparece=0

for i in frase:
    if i == letra:
        vecesAparece+=1

print(vecesAparece)