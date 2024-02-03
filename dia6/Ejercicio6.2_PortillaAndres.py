##Concepts
"""
Strings:Cadena formada por secuencia de caracteres
    Mutable: Si permiten ser modificados una vez creados+
    inmutable: Si no permiten ser modificados una vez creados
"""
##Ejemplo inmutable
Holamundo=str
print=Holamundo
##Ejemplo mutable
z=str(input("Digit the string: "))
print(z)

"""
List:Tipo de dato que permite crear colecciones de datos

"""
a = [90, "Python", 3.87]
print(a[0]) #90
print(a[1]) #Python
print(a[2]) #3.87
##Acceder elementos
## ultimo elemento con el indice [-1]
a = [90, "Python", 3.87]
print(a[-1]) #3.87
##penultimo elemento con el indice[-2]
print(a[-2]) #Python
##modificar valores con el operador =
a[2] = 1
print(a) #[90, 'Python', 1]
##eliminar elementos
l = [1, 2, 3, 4, 5]
del l[1]
print(l) #[1, 3, 4, 5]
##listas anidadases decir, una lista dentro de otra. 
# Incluso podemos tener una lista 
# dentro de otra lista y a su vez dentro de otra lista.
# Para acceder a sus elementos sólo tenemos que usar []
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0])    #p
print(x[3][2][0]) #5
print(x[3][2][2]) #7
##Crear sublistas:Para ello debemos de usar : 
# entre corchetes, indicando a la
# izquierda el valor de inicio,
# y a la izquierda el valor final que no está incluido.
l = [1, 2, 3, 4, 5, 6]
print(l[0:2]) #[1, 2]
print(l[2:6]) #[3, 4, 5, 6]
"""
Tuplas:Las tuplas en Python son un tipo o estructura de datos
que permite almacenar datos de una manera muy parecida a
las listas, con la salvedad de que son inmutables.
"""
##Crear tupla
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)
#or declararse de la siguiente manera
tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)
##iterar tuplas y listas
tupla = [1, 2, 3]
for t in tupla:
    print(t) #1, 2, 3
"""
Dicionario:Los diccionarios en Python
son una estructura
de datos que permite
almacenar su contenido en forma de llave y valor
"""
##Crear diccionario:
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}
##modificar elementos
d1['Nombre'] = "Laura"
print(d1)
#{'Nombre': Laura', 'Edad': 27, 'Documento': 1003882}
##iterar diccionarios
# Imprime los key del diccionario
for x in d1:
    print(x)
#Nombre
#Edad
#Documento
#Direccion
##-------------------------
# Impre los value del diccionario
for x in d1:
    print(d1[x])
#Laura
#27
#1003882
#Calle 123
##-----------------------
# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Laura
#Edad 27
#Documento 1003882
#Direccion Calle 123
"""
MUTABILITY
Sabida ya la clasificación, tal vez te preguntes porqué es esto relevante. Pues bien, 
Python trata de manera diferente a los tipos mutables e inmutables, y si no entiendes 
bien este concepto, puedes llegar a tener comportamientos inesperados en tus programas.

La forma más sencilla de ver la diferencia, es usando las listas en oposición a las tuplas. 
Las primeras son mutables, las segundas no.

Una lista l puede ser modificada una vez creada.
"""
# La asignación se puede realizar
l = [1, 2, 3]
l[0] = 0
##Como hemos explicado antes, id() nos devuelve un identificador único del objeto. Como puedes observar, 
# es el mismo antes y después de realizar la modificación.
l = [1, 2, 3]
print(id(l)) #4383854144
l[0] = 0
print(id(l)) #4383854144
#Sin embargo, una tupla es inmutable, por lo que la siguiente asignación dará un error.
# La asignación no se puede realizar
t = (1, 2, 3)
t[0] = 0
"""
Aunque la tupla es inmutable, si que habría una forma de modificar el valor de t, pero lo que en realidad hacemos es crear una nueva tupla y asignarle el mismo nombre.

Se podría hacer algo como lo siguiente, convertir la tupla en lista, modificar la lista y convertir a tupla otra vez.
"""
t = (1, 2, 3)
print(id(t)) #4483581184
t = list(t)

# Modificar elemento
t[0] = 0

t = tuple(t)
print(t)     #(0, 2, 3)
print(id(t)) #4483953088