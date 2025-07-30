import re
from pydoc import stripid

mensaje = "Prueba python - el curso de nuevas tecnologías"

print(mensaje)

print(f'El largo del mensaje es de {len(mensaje)}')
'''Mayúsculas'''
print(mensaje.upper())
'''Minúsculas'''
print(mensaje.lower())
'''Nombre propio'''
print(mensaje.title())
'''Imprimiar cantidad de letras de la variable'''
espacios = "Hola      estamos          probando             strip"
print(f'La cantidad de letras de la variable es de: {len(espacios)}')

cadena_sin_espacios = re.sub(r'\s+', ' ', espacios).strip()

print(cadena_sin_espacios)