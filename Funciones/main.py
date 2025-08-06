from enum import nonmember


def saludar():
    print("Holaaaaaaaaaaaaaaaaaaaaa")

def saludarName(nombre):
    print(f'Hola {nombre}, cómo estás?')

def porDefecto(nombre, nota, asignatura="Nuevas Tecnologías"):
    print(f'Nombre: {nombre}')
    print(f'Nota: {nota}')
    print(f'Asignatura: {asignatura}')

def operaciones(nro1,nro2,operador):
    if operador == 1:
        return nro1+nro2
    elif operador ==2:
        return nro1-nro2
    elif operador ==3:
        return nro1*nro2
    elif operador ==4:
        if nro2 == 0:
            return "error Div por cero"
        else:
            return nro1/nro2
    else:
        return "Entre 1 y 4"



if __name__ == '__main__':
    nro1 = float(input("Número 1: "))
    nro2 = float(input("Número 2: "))
    operador = int(input("1. Suma\n 2. Resta\n 3. Multiplicar\n 4. Dividir "))

    resultado = operaciones(nro1=nro1,nro2=nro2,operador=operador)
    print(f'El resultado es: {resultado}')

    '''
    saludar()
    saludarName('Luis')
    porDefecto('Luis',4.9)
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))
    asignatura = input("Asignatura: ")
    porDefecto( nombre, nota)
    '''