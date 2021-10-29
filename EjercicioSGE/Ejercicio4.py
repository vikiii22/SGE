nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo (F)emenino/(M)asculino: ")

if (nombre < "M" and sexo == "F") or (nombre < "N" and sexo == "M"):
    print("Perteneces al grupo DAM A")
else:
    print("Perteneces al grupo DAM B")
