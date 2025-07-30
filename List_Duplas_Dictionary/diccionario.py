'''
Un diccionario en Python es una colección de pares clave-valor (key-value pairs). Imagina un diccionario de verdad, donde cada palabra (la clave) tiene una definición (el valor). En Python, funciona de la misma manera:

Cada clave debe ser única e inmutable (generalmente cadenas de texto, números o tuplas).

Cada valor puede ser de cualquier tipo de dato (números, cadenas, listas, otras tuplas, incluso otros diccionarios).

Los diccionarios se definen utilizando llaves {} y los pares clave-valor se separan por dos puntos : y cada par por una coma ,.
'''

# Un diccionario vacío
diccionario_vacio = {}

# Un diccionario con datos
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Medellín",
    "hobbies": ["leer", "viajar", "programar"],
    "contacto": {"email": "ana@ejemplo.com", "telefono": "3001234567"}
}
print(persona)

print(f'hobbies actuales: {persona["nombre"]}')

persona["Barrio"]="Antioquia"
print(persona)

#Modificar contenido
persona["nombre"] = "Valentina"
print(persona)

#Imprimir diccionario
print("Claves del diccionario: ")
for clave, valor in persona.items():
    print(f'{clave}: {valor}')