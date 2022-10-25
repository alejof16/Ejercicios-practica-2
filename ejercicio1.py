def funcion (numero,termino):
    resultado= ""
    for i in range(1,termino+1):
     resultado +="+"+numero*i
    return resultado
num = str (input("ingrese el numero: "))
ter = int (input("ingrese el termino: "))
print(funcion (num, ter))
print(eval(funcion (num, ter)))

