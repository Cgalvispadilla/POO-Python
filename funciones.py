# se importan el modulo operator para usar el methodcaller
from operator import itemgetter, attrgetter, methodcaller
# función para pedir el numero en el menu
def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

# metodo para validar si existe o no un vehiculo ya agregado
def validarVehiculo(placa, listVehiculo):
    existe = False
    for i in listVehiculo:
        if i.getMatricula() == placa:
            existe = True
    return existe

# Este metodo solo funciona para realizar busquedas en listas sencillas o de algun tipo primitivo de dato
# No usarse en listas complejas porque no funciona
# def Validad(dato, lista):
# return dato in lista

# metodo que busca un vehiculo, el cual resive como parametro el dato por el cual desea buscarlo
# y la lista donde se desea buscar a esté


def buscarVehiculoPlaca(dato, listVehiculo):
    buscador = None  # SIEMPRE CREAR UNA VARIABLE CAMBIANTE ANTES DEL METODO
    # se recorre la lista
    for i in listVehiculo:
        # validamos que el vehiculo con el dato que se solicito exista
        if i.getMatricula() == dato:  # AQUI SE VALIDA LA PRIORIDAD DE ENCONTRAR LA MATRICULA
            # si existe se guarda en una variable y se retorna
            buscador = i
            break
        else:
            buscador = False
    return buscador        
    #if buscador == None:
    #    return False
    #else:
    #    return buscador
# nota: CON PYTHON NO SE RECOMIENDA VALIDAR LAS OPCIONES NO ESPERADAS DENTRO DEL CICLO FOR
# SOLO VALIDAR LA ESPERADA Y VALIDAR FUERA DEL CICLO TODAS LAS QUE NO SEAN DE NUESTRA PRIORIDAD
#Nota 2: sirve si y solo si de la manera anterior si se rompe el ciclo en la condición esperada

# la manera más optima segun el Porti y Carlos del metodo sería porque toda sentencia de control (ciclo) en python tiene UNA CONTINUACION
# "else" para validar lo contrario a lo que se desea hacer con el ciclo
# def buscarVehiculoPlaca(dato, listVehiculo):
#    buscador = None #SIEMPRE CREAR UNA VARIABLE CAMBIANTE ANTES DEL METODO
    # se recorre la lista
#   for i in listVehiculo:
        # validamos que el vehiculo con el dato que se solicito exista
#        if i.getMatricula() == dato: #AQUI SE VALIDA LA PRIORIDAD DE ENCONTRAR LA MATRICULA
        # si existe se guarda en una variable y se retorna
#            buscador = i
#            return buscador
#   else:
#       return False

# metodo para ordenar la lista


def ordenar(dato, listVehiculo):
    # se valida el porque se desea
    if(dato == "precio" or dato == "Precio"):
        # sorted(listVehiculo, key=itemgetter(0))
        listVehiculo.sort(key=methodcaller('getPrecio'), reverse=True)
        # sorted(listVehiculo, key=lambda vehiculo: vehiculo.matricula)
    elif dato == "Marca" or dato == "marca":
        listVehiculo.sort(key=methodcaller('getMarca'), reverse=True)
