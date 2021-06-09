from operator import itemgetter, attrgetter, methodcaller
from os import umask
#se importa el modulo de vehiculo
from Vehiculo import *
#se importa el modulo de las funciones
from funciones import *

def agregar_vehiculo(Vehiculo):
    try:
        with open("vehiculos.txt",'a', encoding="utf8") as archivo:
            archivo.write(Vehiculo.getMatricula()+" "+Vehiculo.getMarca()+" "+Vehiculo.getModelo()+" "+str(Vehiculo.getPrecio())+" "+str(Vehiculo.getEstado())+" \n")
    except Exception as e:
            print(e)   

def pasar_vehiculos_lista():
        unVehiculo: Vehiculo
        try:
            with open("vehiculos.txt",'r', encoding="utf8") as archivo:
                for pelicula in archivo:
                    dividir= pelicula.split(" ")
                    matricula=dividir[0]
                    marca=dividir[1]
                    modelo=dividir[2]
                    precio=dividir[3]
                    estado=dividir[4]
                    unVehiculo= Vehiculo(matricula, marca, modelo, precio,estado)
                    listVehiculo.append(unVehiculo)
        except Exception as e:
            print(e)            
            
listVehiculo = []
pasar_vehiculos_lista()
print(listVehiculo)
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
                agregar_vehiculo(miVehiculo)
                listVehiculo.append(miVehiculo)
            elif est == "disponible":
                miVehiculo = Vehiculo(m, mar, mo, pre, False)
                listVehiculo.append(miVehiculo)
                agregar_vehiculo(miVehiculo)
            else:
                print("error, debes poner vendido o disponible ;)")

    elif opcion == 2:
        if listVehiculo:
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
