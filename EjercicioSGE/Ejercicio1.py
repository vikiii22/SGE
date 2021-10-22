cont="contraseña"
entrada=input("Contraseña?: ")


if entrada==cont or entrada.capitalize()==cont.capitalize():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")