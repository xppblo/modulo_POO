"""
ABSTRACCION
Una clase va a ser abstracta si tiene al menos un metodo abstracto

Metodo Abstracto:
Son aquellos que solamente tienen la definicion del metodo
ademas debe tener el decorador @abstractmethod

para poder crear una clase abstracta y un metodo abstracto importamos:

from abc import ABC, abstractmetod
"""

from abc import ABC, abstractmethod

class Pelota(ABC):#Clase abstracta
    
    @abstractmethod
    def rebotar(self, altura : int):
        pass
    #Obligacion dee crear ele metodo abstracto
    
    
class PelotaDeJuguete(Pelota):
    def __init__(self):
        self.color = "Blanco"
          
    def rebotar(self, altura : int):
        pass
    
pelotita = PelotaDeJuguete() # TypeError: Can't instantiate abstract class PelotaDeJuguete without an implementation for abstract method 'rebotar'
print(pelotita.rebotar(20))