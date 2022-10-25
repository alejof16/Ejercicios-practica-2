def agregar_dairy(dairy,nombre,existencia):
    productos={}
    productos['nombre']= nombre
    productos['existencia']= existencia
    dairy.append(productos)   
def mostrar_inventario(dairy):
    for i in dairy:
        print(f"NOMBRE: {i['nombre']}, EXISTENCIA: {i['existencia']}" )
def agregar_aseo(cleaning,nombre,existencia):
    productos={}
    productos['nombre']= nombre
    productos['existencia']= existencia
    cleaning.append(productos)

def mostrar_inventario2(cleainig):
    for i in cleainig:
        print(f"NOMBRE: {i['nombre']}, EXISTENCIA: {i['existencia']}" )

def agregar_grano(grain,nombre,existencia):
    productos={}
    productos['nombre']= nombre
    productos['existencia']= existencia
    grain.append(productos)

def mostrar_inventario3(grain):
    for i in grain:
        print(f"NOMBRE: {i['nombre']}, EXISTENCIA: {i['existencia']}" )


dairy = []
cleaning =[]
grain = []
while True:
    print("Inventario de productos")
    print("=============================")
    print("1. agregar articulo al inventario")
    print("2. ver el inventario")
    print("3. salir")
    opcion = int(input("Digite una opción: "))

    print()

    if opcion == 1:
        print("\nAgregar nuevo articulo \n")
        opcion = int(input("Grupos \n 1.dairy \n 2.cleaning \n 3.grain \n seleccione el grupo:" ))
        if (opcion==1):
            print("\n grupo dairy\n")
            nombre= input("ingrese el nombre del producto:")
            existencia= input("ingrese el numero de exstencias:")
            agregar_dairy( dairy,nombre,existencia)
        if (opcion==2):
            print("\n grupo cleaning\n")
            nombre= input("ingrese el nombre del producto:")
            existencia= input("ingrese el numero de exstencias:")
            agregar_dairy( cleaning,nombre,existencia)
        if (opcion==3):
            print("\n grupo de grain\n")
            nombre= input("ingrese el nombre del producto:")
            existencia= input("ingrese el numero de exstencias:")
            agregar_dairy( grain,nombre,existencia)
    elif opcion==2:
        print("\nVer Inventario \n")
        opcion = int(input("Grupos \n 1.dairy \n 2.cleaning \n 3.grain \n seleccione el grupo:" ))
        if (opcion==1):
         mostrar_inventario(dairy)
        if (opcion==2):
         mostrar_inventario2( cleaning)
        if (opcion==3):
         mostrar_inventario3(grain)


    elif opcion ==3:
        break
    print ( " fin del inventario")
    print ()
    

