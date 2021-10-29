persona = {}
sigue=True

while sigue:
    clave=input("Dato a introducir: ")
    valor=input(clave + ': ')
    persona[clave]=valor
    print(persona)
    sigue=input("Desea añadir algo más?: ") == "Si"