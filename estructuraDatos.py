import random

print("Estructura de datos")

print("%s es muy sabio" % "Ferb")
print("%s sabe %i idiomas" % ("Perry", 5))

nombre = ["Melisa", "Maria", "Luis", "Rafa"]
print(nombre[-1])
print(nombre[-2:])

tutifruti = [1.2, "Jairo", (12e6, nombre[0])]
print(tutifruti)

unaTupla = ("Martín", 1.2, (1j, nombre[1]))
print(unaTupla)

print(type(tutifruti))
print(unaTupla[1:3])

sub_tupla = tuple(unaTupla[2])
sub_lista = list(unaTupla[2])
print("subtupla ", sub_tupla)
print("sublista ", sub_lista)

tutifruti[0] = "no se"
print(tutifruti)

tutifruti.extend([unaTupla])
print(tutifruti)

#unaTupla[-1]="Osoo"
#unaTupla.append('a')

l=[1,2,3,4]
t=(1,5,8,1)
print(l.count(1))
print(t.count(1))
l.append('8')
print(l)

print(list(range(3,10,2)))
print(list(range(3,11,2)))
print(list(range(3,12,2)))
print(list(range(1,20,5)))

a = [1, 'hola', []]
print(a.index('hola'), "Esto es index")
a.reverse()
print(a)

a=[1,2,3]
a.reverse()
print(a)

print(list(reversed(a)))
print(a)

b=list(reversed(a))
print(b, a)

print(sum(b))
print(max(b))
print(min(b))

#Desempacar buscar info
print("----Desempacar List-----")
#Asigna cada letra a un valor asignado
a,b,c=(1,2,5)
print(a)
print(b)
print(c)
print("-------Desempacar String--------")
a,b,c="123"
print(a)
print(b)
print(c)

print("--------Viernes 15 de Octubre---------")
#Aprendiendo dict
user={'nick':'neo', 'phone':'5555'}
print(list(user.keys()))
print(list(user.values()))

print('nick' in user)

user.update({'nick':'altair', 'age':'20'})
print(user)

print(list(user.keys()))
user.update({'nick':'Jose'})
print(user)
print('Jose' in user.values())

num=random.randint(20,100)
user.update({'age':num})
print(user)

print(sorted(user))

print(list(user.items()))
print(user.pop("nick"))

#Estructura de datos set