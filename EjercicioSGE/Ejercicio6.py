usuario = "puri"
usuarioIntroducido = input("Introduce tu nombre de usuario: ")
contrasenya = "calzadosPuri"
intentos = 0

while usuarioIntroducido != usuario:
    intentos += 1
    print("Usuario incorrecto")
    usuarioIntroducido = input("Introduce el nombre de usuario: ")
    if intentos > 3:
        print("Has usado demasiados intentos, hasta luego")
        exit()
if usuarioIntroducido == usuario:
    intentos = 0
    contrasenyaIntro = ''
    while contrasenyaIntro != contrasenya:
        contrasenyaIntro = input("Introduce la contraseña: ")
        intentos += 1
        if intentos > 3:
            print("Has usado demasiados intentos, hasta luego")
            exit()
        elif contrasenyaIntro == contrasenya:
            print("Bienvenida " + usuario)
