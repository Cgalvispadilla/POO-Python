from operator import itemgetter, attrgetter, methodcaller
#se importa el modulo de vehiculo
from Vehiculo import *
#se importa el modulo de las funciones
from funciones import *
        
listVehiculo = []
salir = False
opcion = 0
sol = None
while not salir:
    
    print("1. Agregar Vehiculo")
    print("2. Mostrar todos los vehiculos")
    print("3. Buscar Vehiculo")
    print("4. ordenar por precio")
    print("5. ordenar por marca")
    print("6. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        m = input('Ingrese la placa del vehiculo: ')
        enc = validarVehiculo(m, listVehiculo)
        if enc == True:
            print("Ya esta el vehiculo, intenta con otro ;)")
        else:
            mar = input('Ingrese la marca del vehiculo: ')
            mo = input('Ingrese el modelo del vehiculo: ')
            pre = float(input('Ingrese el precio del vehiculo: '))
            est = input('Ingrese el estado del vehiculo (vendido o disponible): ')
            if est == "vendido":
                #objeto de la clase vehiculo
                miVehiculo = Vehiculo(m, mar, mo, pre, True)
                listVehiculo.append(miVehiculo)
            elif est == "disponible":
                miVehiculo = Vehiculo(m, mar, mo, pre, False)
                listVehiculo.append(miVehiculo)
            else:
                print("error, debes poner vendido o disponible ;)")

    elif opcion == 2:
        for i in listVehiculo:
            print("matricula",i.getMatricula(), "modelo", i.getModelo(), "precio", i.getPrecio())
        else:
            print('no hay vehiculos aún')
    elif opcion == 3:
        pla = input('Ingrese la placa del vehiculo que desea buscar:')
        sol = buscarVehiculoPlaca(pla, listVehiculo)
        if sol != False:
             print("Placa: "+ sol.getMatricula() + " marca: "+ sol.getMarca() + " modelo: "+sol.getModelo()+" Precio: ",sol.getPrecio())
        else: 
            print('el auto no existe en el concesionario')
    elif opcion == 4:
        ordenar("Precio",listVehiculo)
        for i in listVehiculo:
            print("matricula",i.getMatricula(), "modelo", i.getModelo(), "precio", i.getPrecio())
        else: 
            print('el auto no existe en el concesionario')
    elif opcion == 5:
        ordenar("Marca",listVehiculo)
        for i in listVehiculo:
            print("matricula",i.getMatricula(), "modelo", i.getModelo(), "precio", i.getPrecio())
        else: 
            print('el auto no existe en el concesionario')    
    elif opcion == 6:
        salir = True
    else:
        print("Introduce un numero entre 1 y 6")
