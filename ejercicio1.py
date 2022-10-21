
def funcion (numero,termino):
    resultado= ""
    for i in range(1,termino+1):
     resultado +="+"+numero*i
    print(resultado)
    print(eval(resultado))
num = str (input("ingrese el numero: "))
ter = int (input("ingrese el termino: "))
funcion (num, ter)
