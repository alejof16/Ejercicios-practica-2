
lista = [8,1,2,3,4,4,4,6,7,7,2]
def agruparsimilares(lista):
    unicos= list(set(lista))
    unicos_2 = []
    for i in lista:
        if not (i in unicos_2 and i in unicos):
            unicos_2.append(i)
    respuesta = []
    for i in unicos_2:
        aux = []
        for j in lista:
            if i ==j:
             aux.append(i)
        respuesta.append(aux)
    print(respuesta)
agruparsimilares(lista)
