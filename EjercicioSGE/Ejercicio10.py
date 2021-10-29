dict = {'Mandarina': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}

elegido = input("Elige una fruta: ")
kg = int(input("Cuantos kilos?: "))
seguir = True
aPagar = 0
frutasElegidas = ''

while seguir:
    if elegido in dict.keys():
        print("Has elegido " + elegido + " el kg son:", dict.get(elegido), " tienes que pagar: ",
              dict.get(elegido) * kg, "€")
        aPagar += dict.get(elegido) * kg
        frutasElegidas += elegido + " "

    else:
        print(elegido + " no disponible")
    seguir = input("Quiere seguir comprando? ")
    if seguir == "no":
        print("Has elegido " + frutasElegidas)
        print("Total a pagar: ", aPagar)
        exit()
    else:
        elegido = input("Elige una fruta: ")
        kg = int(input("Cuantos kilos?: "))
