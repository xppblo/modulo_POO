class Madre():
    def __init__(self, color : str):
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color : str):
        self.__color = color
        
class Padre():
    def __init__(self, tamanio : int):
        self.__tamanio = tamanio

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio : int):
        self.__tamanio = tamanio
        
class Hija(Padre, Madre):
    pass

princesa = Hija("Morado")

princesa.tamanio = 10
print(princesa.tamanio)