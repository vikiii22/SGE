#No funciona bien, he tenido que mirar en la página para guiarme un poco

usuarios="nif;nombre;email;teléfono;descuento\n" \
         "01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n" \
         "71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n" \
         "63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n" \
         "98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

divididos=usuarios.split("\n")
directorio={}
campos=divididos[0].split(";")

for i in divididos[1:]:
    usuario={}
    infoUsu=i.split(';')
    for j in range(1,len(campos)):
        if campos[j]=='descuento':
            infoUsu[j]=float(infoUsu[j])
        usuario[campos[j]]=infoUsu[j]
    directorio[infoUsu[0]]=usuario
print(usuario)