#Creando una lista con list()
lista = list(["Hola","Caballero",35])

#devuelve la cantidad de elementos de la lista
resultado1 = len(lista)

#agregando un elemento a al lista
lista.append("jajja")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"toma mama")

#agregando varios elementos a la lista
lista.extend([False, 2002])

#eliminando un elemento de la lista (por su indice), si no se le da un indice elimina el ultimo
lista.pop()

#remueve un elemento de la lista por su valor
lista.remove("toma mama")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente y solo funciona con numeros(si usamos el parametro reverse = True lo ordena en reversa)
#lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()
print(lista)