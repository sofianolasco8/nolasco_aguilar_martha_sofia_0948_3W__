print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
print(" ")
# se crea un diccionario
precios = {
    'manzana': 25.5,
    'banana': 16.9,
    'naranja': 30.5,
    'uva': 40.6,
}

# indicar al usuario ingresar la fruta y los kilos 
fruta = input("ingresa la fruta que desee  ")
kilos = float(input("Introduce los kilos que desee "))

# Verificar si la fruta está en el diccionario
if fruta in precios:
    total = precios[fruta] * kilos
    print("El precio de la fruta es", total)
else:
    print("No tenemos esa fruta.")
