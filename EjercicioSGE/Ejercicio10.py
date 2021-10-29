dict={'Plátano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}

elegido=input("Elige una fruta: ")
kg=int(input("Cuantos kilos?: "))

if elegido in dict.keys():
    print("Has elegido " + elegido + " el kg son:", dict.get(elegido), " tienes que pagar: ", dict.get(elegido) * kg, "€")
else:
    print(elegido+" no disponible")