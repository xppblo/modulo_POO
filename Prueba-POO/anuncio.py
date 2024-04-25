from abc import ABC, abstractmethod

class Anuncio(ABC):
    def __init__(self, ancho : int, alto : int, url_archivo : str, url_clic : str, sub_tipo : str):
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho : int):
        self.__ancho = ancho
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto : int):
        self.__alto = alto
    
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo : str):
        self.__url_archivo = url_archivo
        
    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url_clic : str):
        self.__url_clic = url_clic
        
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo : str):
        self.__sub_tipo = sub_tipo
        
    def mostrar_formatos(self):
        pass
        
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self, duracion : int):
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = duracion
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho : int):
        self.__ancho = ancho
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto : int):
        self.__alto = alto
        
    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion : int):
        self.__duracion = duracion
        
    def comprimir_anuncio(self):
        return super().comprimir_anuncio()
    
    def redimensionar_anuncio(self):
        return super().redimensionar_anuncio()
    
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    
    def comprimir_anuncio(self):
        return super().comprimir_anuncio()
    
    def redimensionar_anuncio(self):
        return super().redimensionar_anuncio()
    
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPO = ("facbook", "linkedin")
    
    def comprimir_anuncio(self):
        return super().comprimir_anuncio()
    
    def redimensionar_anuncio(self):
        return super().redimensionar_anuncio()