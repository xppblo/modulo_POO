from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho : int, alto : int, url_archivo : str, url_clic : str, sub_tipo : str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if ancho > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        
        
    #getter  and setter
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho : int):
        self.__ancho = ancho if ancho > 0 else 1
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto : int):
        self.__alto = alto if alto > 0 else 1
    
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
    def sub_tipo(self, sub_tipo):
        if(isinstance(self,Video)  and sub_tipo not in Video.SUB_TIPOS or
           isinstance(self,Display)  and sub_tipo not in Display.SUB_TIPOS or
           isinstance(self,Social)  and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError(f"El subtipo {sub_tipo} no es un subtipo de video")
        else:
            self.__sub_tipo = sub_tipo
        
    #metodos
    
    @staticmethod
    def mostrar_formatos():
        print("FORMATO VIDEO:")
        print("==========")
        for sub_tipo in Video.SUB_TIPOS:
            print(f"- {sub_tipo}")            
        print()        
        print("FORMATO DISPLAY:")
        print("==========")
        for sub_tipo in Display.SUB_TIPOS:
            print(f"- {sub_tipo}")            
        print()        
        print("FORMATO SOCIAL:")
        print("==========")
        for sub_tipo in Social.SUB_TIPOS:
            print(f"- {sub_tipo}")
        
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion : int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = duracion if duracion > 0 else 5
                    
    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion : int):
        self.__duracion = duracion if duracion > 0 else 5
        
    #sobre escritura de los metodos getter y setter de la clase Padre
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho : int):
        pass
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto : int):
        pass
        
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE ANUNCIO NO IMPLEMENTADO AÚN")
    
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facbook", "linkedin")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")