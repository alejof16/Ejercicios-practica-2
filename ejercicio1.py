print ("ingrese el numero")
numero = str (input())
print ("ingrese el termino")
termino = int (input())
resultado = ""
for i in range(1,termino+1):
    resultado +=  "+"+numero*i

print (resultado)
print(eval(resultado))
