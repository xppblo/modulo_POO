class Auto():
    def __init__(self, color : str = "blanco"):
        self.__color = color
        
    def __str__(self):
        return f"Metodo sobre cargado, color : {self.__color}"
        
masserati = Auto()
print(masserati)#<__main__.Auto object at 0x000001AED5066330>

mercedes = Auto("Negro")
print(mercedes)