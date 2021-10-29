compra = {}
sigue = True

while sigue:
    clave = input("Producto a introducir: ")
    valor = int(input(clave + ' precio: '))
    compra[clave] = valor
    sigue = input("Desea añadir algo más?: ") == "si"

print("-----LISTA-----")
total = 0
for i in compra:
    print(i, compra.get(i), "€")
    total += compra.get(i)

print("------Total-------")
print("Total a pagar:", total, "€")
