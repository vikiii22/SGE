usuario = {}
opcion = ''

while opcion != '6':
    if opcion == '1':
        nif = input("Introduce tu DNI: ")
        nombre = input("Introduce tu nombre: ")
        direccion = input("Introduce tu dirección: ")
        telefono = input("Introduce tu teléfono: ")
        email = input("Introduce tu correo: ")
        vip = input("Eres VIP (si|no): ")
        usuario = {'nombre': nombre, 'dirección': direccion, 'teléfono': telefono, 'email': email, 'VIP': vip == 'si'}
        usuario[nif] = usuario
    if opcion == '2':
        nif = input("Introduce tu DNI: ")
        if nif in usuario:
            del usuario[nif]
        else:
            print("Este usuario no existe")
    if opcion == '3':
        nif = input("Introduce tu DNI: ")
        if nif in usuario:
            print('nif:', nif)
            for clave, valor in usuario[nif].items():
                print(clave.title() + ':', valor)
        else:
            print("No existe el cliente")
    if opcion == '4':
        print("-----LISTA CLIENTES------")
        for clave, valor in usuario.items():
            print(clave, valor)
    if opcion == '5':
        print("-----LISTA VIP-----")
        for clave, valor in usuario.items():
            if clave == 'VIP':
                print(clave, valor)
    opcion = input('Menú de opciones\n'
                   '(1) Añadir cliente\n'
                   '(2) Eliminar cliente\n'
                   '(3) Mostra cliente\n'
                   '(4) Listar clientes\n'
                   '(5) Listar clientes preferentes\n'
                   '(6) Terminar\n')
