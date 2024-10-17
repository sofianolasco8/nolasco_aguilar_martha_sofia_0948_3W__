print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
# indicar al usuario ingresar los datos
nombre = input("Ingresa tu nombre ")
edad = input("cual es tu edad ")
direccion = input("ingresa tu direccion ")
telefono = input("cual es tu telefono ")

# Crea un diccionario con los datos 
info = {}
info['nombre'] = nombre
info['edad'] = edad
info['direccion'] = direccion
info['telefono'] = telefono

# muestra los datos al usuario 
print(f"{info['nombre']},")
print(f" tiene {info['edad']} años,")
print(f"vive en {info['direccion']},")
print(f"y su número de teléfono es {info['telefono']}.")
