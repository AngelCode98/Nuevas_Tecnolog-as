'''
Crear una función que agregue elementos a una lista llamada nombres, debe retornar la lista
Crear una función que imprima la lista anterior
'''

def llenar_lista(lista):
    print("Escribe fin para terminar de agregar a la lista")

    while True:
        dato = input("Ingrese un dato para la lista: ")

        if dato.lower() == "fin":
            break

        lista.append(dato)

if __name__ == '__main__':
    pass

mi_lista = []

llenar_lista(mi_lista)

print(f'La lista es la siguiente: {mi_lista}')