diccionario = {
    "nombre" : "Lucas",
    "apellido" : "Caballero",
    "subs" : 1000
}


#devuelve las claves (tambien nos sirve para iterar), sino encuentra nos tira una excepcion
diccionario.keys()

#le tenemos que pasar una key y nos devuelve el valor, sino encuentra nos tira un "None"
clave = diccionario.get("nombre")

#Elimina todos los elementos del diccionario
#diccionario.clear()

#Elimina un elemento del diccionario
#diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)