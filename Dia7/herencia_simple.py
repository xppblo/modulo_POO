class Padre():
    #atributo de clase
    color = "verde"
    #constructor
    def __init__(self, tamanio : int):
        #atributos de instancia
        self.__tamanio = tamanio
    #metodos estaticos
    #metodos de instancia
    def cambiar_color(self, color: str):
        if color != "":
            self.color = color
    #sobrecarga
    def __str__(self):
        return f"El color es {self.color}, y de tamanio {self.__tamanio}"
    #getter - setters
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio :int):
        if tamanio > 0:
            self.__tamanio = tamanio
        else:
            self.__tamanio = 0
         
#Herencia

class Hija(Padre):
    peso = 100
    
class Hijo(Padre):
    deuda = 120

class Nieto(Hija):
    pass

#Instancia de la clase
hijita = Hija(100)
print(f"el color de la clase hija ees {hijita.color}")

regalon = Nieto()
panial = "XL"