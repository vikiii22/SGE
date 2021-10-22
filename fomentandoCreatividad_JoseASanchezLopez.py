import math

print(round(5.6))
print(round(math.pi, 4))
print(math.ceil(5.4))
print(math.trunc(5.8))

nombres=['Juan', 'Martín', 'María']
pasiones=['Cerveza', 'boca juniors', 'lechuga']
nacionalidad = ('Me gustas', 'El boquitas', 'No me gusta')
combi=list(zip(nombres, pasiones, nacionalidad))
print(combi)#crea lista con tres tuplas

print("python mola"[1:4])
print("python mola".find("mola"))
print("python mola".replace("python", "php no"))
print("python mola".split(" "))
print(" ".join(["python", "mola"]))

print("------------------------------------")

v="hola amigos"

print(v.upper())
t=",¿Cómo están ustedes?"
print(v + t)
print("*"*4)

a="hola,amigos,como"
nombre="Pedro#Juan#Lara"
lista=nombre.split("#")
print("Nombre: "+lista[0])
print("Apellidos: " + lista[1], lista[2])
print(nombre.replace("#", " "))

cadena="Hola mundo"

texto="{} es {}".format("Messi", "crack")
print(texto)
textos="{1} es {0}".format("Messi", "crack")
print(textos)
#textoss="{saludo} {planeta}".format(saludo="Hola", planeta="mundo") la dejo comentada porque da error.

print("Introduce un texto: ")
textoIntroducido=input()
print(textoIntroducido.upper())
print(textoIntroducido.lower())
print(textoIntroducido.capitalize())
print(textoIntroducido.replace(" ", " ¬ "))
print(textoIntroducido.split(" "))
print(len(textoIntroducido))

print("Introduce un número: ")
numeroIntroducido=int(input())
print("Introduce otro: ")
numeroIntroducido2=int(input())

print("Division:", numeroIntroducido // numeroIntroducido2)
print("Resto:",numeroIntroducido % numeroIntroducido2)
print("Multiplicación:",numeroIntroducido * numeroIntroducido2)
print("{}".format("Suma:"),numeroIntroducido + numeroIntroducido2)
