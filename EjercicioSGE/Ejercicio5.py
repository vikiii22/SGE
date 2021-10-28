renta = int(input("Introduce tu renta anual: "))

if renta < 10000:
    resultado = renta * 5 / 100
elif renta >= 10000 and renta <= 20000:
    resultado = renta * 15 / 100
elif renta >= 20000 and renta <= 35000:
    resultado = renta * 20 / 100
elif renta >= 35000 and renta <= 60000:
    resultado = renta * 30 / 100
elif renta > 60000:
    resultado = renta * 45 / 100

print("Tienes que pagar {:.0f}".format(resultado))
