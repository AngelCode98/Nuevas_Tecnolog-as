'''
Listas:
Puntos clave sobre las listas en Python:
Ordenadas: Los elementos en una lista tienen un orden específico que se mantiene.
Mutables: Los elementos de una lista pueden ser modificados, agregados o eliminados.
Heterogéneas: Una lista puede contener elementos de diferentes tipos de datos (enteros, cadenas, booleanos, etc.).
Índices: Los elementos se acceden a través de sus índices, comenzando por 0 para el primer elemento.

Creación de listas:
# Lista vacía
lista_vacia = []

# Lista con elementos
mi_lista = [1, "hola", 3.14, True]

# Lista utilizando el constructor list()
otra_lista = list((1, 2, 3)) # Crea una lista a partir de una tupla

Acceso a elementos:
Python

mi_lista =

# Acceder al primer elemento (índice 0)
primer_elemento = mi_lista  # 10

# Acceder al último elemento
ultimo_elemento = mi_lista[-1] # 50

# Acceder a un rango de elementos (slice)
sub_lista = mi_lista[1:4] #

Modificación de listas:
Python

mi_lista =

# Modificar un elemento
mi_lista = 10

# Agregar un elemento al final
mi_lista.append(4)

# Insertar un elemento en una posición específica
mi_lista.insert(1, 5)

# Eliminar un elemento por valor
mi_lista.remove(3)

# Eliminar un elemento por índice
mi_lista.pop(0)

# Eliminar todos los elementos
mi_lista.clear()
'''

estudiantes = ["Sara", "Catalina", "Susana", "Luis"]
print(estudiantes)
print(f'Tamaño de la lista {len(estudiantes)}')
#Posición
print(f'El valor de la posición es: {estudiantes[2]}')
#Reemplazar contenido por posición
estudiantes[2] = "Angel"
print(estudiantes)
#Imprimir el último de la lista
print(f'El último elemento de la lista es: {estudiantes[-1]}')
#Agregar datos a la lista (Al final)
estudiantes.append("Ramirez")
estudiantes.append("999")
print(estudiantes)
#Lista ordenada
estudiantes.sort()
print(f'Lista ordenada: {estudiantes}')
#Agregar dato en X posición
estudiantes.insert(1,"Andres")
print(estudiantes)
#Eliminar un dato
estudiantes.pop(1)
print(estudiantes)
#Eliminar todos los elementos de la lista
estudiantes.clear()
print(estudiantes)