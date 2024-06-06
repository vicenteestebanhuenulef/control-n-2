lista_palabras = []

palabra = input("ingrese una palabra a la lista: ")
print("(presione enter para terminar ingreso)")

while palabra != "":
    lista_palabras.append(palabra)
    palabra=input("ingrese palabra para agregar a la lista: ")
    print("(presione enter para terminar ingreso)")

for palabra in lista_palabras:
    print (len(palabra))
