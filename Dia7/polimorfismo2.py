class Madre():
    def __init__(self, color : str, **parametros):
        super().__init__(**parametros)
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color : str):
        self.__color = color
        
class Padre():
    def __init__(self, tamanio : int, **parametros):
        super().__init__(**parametros)
        self.__tamanio = tamanio

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio : int):
        self.__tamanio = tamanio
        
class Hija(Padre, Madre):
   #Sobre escritura del metodo constructor
   #def __init__(self,color : str, tamanio: int):
   #    Madre.__init__(self, color)
   #    Padre.__init__(self,tamanio)
   def __init__(self, deuda = 0,**parametro):
       #atributo de instancia propio de hija
       super().__init__(**parametro)
       self.deuda = deuda

#princesa = Hija("Morado",80)
princesa = Hija(color ="Morado", tamanio = 80, deuda = 350)

print(princesa.color, princesa.tamanio, princesa.deuda)