# EJERCICIONUMERO 2

def funcion(num):
  lista =[]
  for i in  num:
    if i >=1000:
      break
    if i <=600:
      if i % 5==0:
         lista.append(i)
  return lista   

numero= [655,150,300,295,1000,55,33]
print(funcion(numero))




                
             
