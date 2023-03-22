cadena1 = "Hola soy Lucas"
cadena2 = "Bienvenido maquinola"

#toda la oracion en mayuscula
resultado = cadena1.upper()

#toda la oracion en minuscula
resultado2 = cadena1.lower()

#primera letra en mayuscula
resultado3 = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1
resultado4 = cadena1.find("H")

#buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepcion
resultado5 = cadena1.index("a")

#si es numerico, devuelve true, sino false
resultado6 = cadena1.isnumeric()

#si es alfanumerico devuelve true, sino false
resultado7 = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
resultado8 = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena, len es una funcion, no es un metodo
resultado9 = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
resultado10 = cadena1.startswith("o")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
resultado11 = cadena1.endswith("a")

#reemplaza un pedazo de la cadena dada, por otra
resultado12 = cadena1.replace("la","lu")

#separar cadenas con la cadena que le pasemos
resultado13 = cadena1.split(" ")
print(resultado,resultado2,resultado3,resultado4,resultado5,resultado6,resultado7,resultado8,resultado9,resultado10,resultado11,resultado12,resultado13)                                                                                       