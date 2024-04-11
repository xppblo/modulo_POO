class Pelota():
    #Atributos de clase
    
    #Constructor
    def __init__(self, color: str, tamanio = 20, material = "plastico"):
        print("Metodo constructor al crear el objeto")
        self.__color = color
        self.tamanio = tamanio
        self.material = material
        self.rebotes = 0
        self.__password = "qwerty"
    
    #Metodo oculto    
    def __getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
        
    def setPassword(self,password):
        self.__password = password
    
    #getter
    @property #da acceso al atributo oculto
              #Lo muestra como una propiedad y permite trabajar como si fuera un atributo y no como metodo  
    def color(self):
        return self.__color
    
    #setter
    @color.setter
    def color(self,color : str):
        self.__color = color if color != "" else "Verde"
        
    @color.deleter
    def color(self):
            del self.__color
    
    
    #Metodo de instancia
    
pelota_futbol = Pelota("amarillo",16,"plastico")
print(pelota_futbol.tamanio, pelota_futbol.material)
print("metodo getter", pelota_futbol.color) # metodo getter amarillo
#print("getColor() ",pelota_futbol.getColor())


#pelota2 = Pelota() TypeError: Pelota.__init__() missing 3 required positional arguments: 'color', 'tamanio', and 'material'

pelota3 = Pelota("Rojo")
#print(pelota3.color) AttributeError: 'Pelota' object has no attribute 'color'
print(pelota3.tamanio, pelota3.material)


#pelota4 = Pelota() TypeError: Pelota.__init__() missing 1 required positional argument: 'color'