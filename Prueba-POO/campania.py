from anuncio import Video,Social,Display

class Campania():
    def __init__(self, nombre : str, fecha_inicio : str, fecha_termino : str, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.instancias_de_anuncios() for dicc in anuncios]
        
    def instancias_de_anuncios(self, anuncio : dict):
        return Video()
        return Display()
        return Social()
    
    def __str__(self) -> str:
        pass