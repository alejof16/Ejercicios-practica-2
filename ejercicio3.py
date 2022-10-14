from itertools import groupby



nombres = [ "camilo","lorena", "camilo","andres","luis", "sofia","lorena"]
nombres.sort()
print(nombres)

print()

resultado = [list(datos) for _, datos in groupby(nombres, lambda  e:e.split("i++")[0])]
print(resultado)