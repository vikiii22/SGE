num1 = int(input("numero1: ")) #El usuario no puede introducir un valor en blanco
num2 = int(input("numero2: "))

division = num1 / num2

if num2 == 0:
    print("Error, introduce algún número")
else:
    print("El resultado es {}".format(division))
