class Vehiculo:
    
    def __init__(self, matricula, marca, modelo, precio, estado):
        self.__matricula = matricula
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio
        self.__estado = estado

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def setPrecio(self, precio):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def setEstado(self, estado):
        self.__estado = estado

    def getEstado(self):
        return self.__estado
