contrasenya="contraseña"
contrasenyaIntro=input("Introduce la contraseña: ")

while contrasenyaIntro.lower() != contrasenya:
    print("Contraseña errónea")
    contrasenyaIntro = input("Introduce la contraseña: ")

print("Bienvenido")
