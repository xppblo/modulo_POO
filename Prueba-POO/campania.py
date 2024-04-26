from anuncio import Video,Social,Display

class Campania():
    def __init__(self, nombre : str, fecha_inicio : str, fecha_termino : str, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.instancias_de_anuncios() for dicc in anuncios]
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def ancho(self, nombre : str):
        self.__nombre = nombre
        
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio : str):
        self.__fecha_inicio = fecha_inicio
    
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def ancho(self, fecha_termino : str):
        self.__fecha_termino = fecha_termino
        
    @property
    def anuncios(self):
        return self.__anuncios
        
    
        
    def instancias_de_anuncios(self, anuncio : dict):
        return Video()
        return Display()
        return Social()
    
    def __str__(self) -> str:
        return """
        Nombre de la campaña:
        Anuncios:
        """