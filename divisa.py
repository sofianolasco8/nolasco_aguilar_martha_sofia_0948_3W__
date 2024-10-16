print(" ")
print("nolasco_aguilar_martha_sofia_0948_3W")
print(" ")
thisdict = { #se abre el diccionario
    "euro": "€",
    "dollar":"$",
    "yen":"¥",
}
divisa = input("ingresa una variable ") #se indica al usuario ingresar una variable 
if divisa in thisdict: #verifica si la divisa esta en el diccionario 
    print("la divisa de",divisa,"es",thisdict[divisa])#si la divisa esta en el diccionario se muestra 
elif divisa != thisdict:#verifica si la divisa no esta en el diccionario 
    print("la divisa no esta dentro del diccionario")#envia un mensaje de error 