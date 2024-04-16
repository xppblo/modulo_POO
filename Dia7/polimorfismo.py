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
    peso = 80
    #polimorfismo, cambio del comportamiento del metodo de la clase padre
    def cambiar_color(self, color: str):
            self.color = color
    
class Hijo(Padre):
    deuda = 120
    def __init__(self, tamanio: int, saldo = 0):
        super().__init__(tamanio) # llamado al constructor del Padre
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

class Nieto(Hija):
    pass

#Instancia de la clase
hijita = Hija(100)
hijita.cambiar_color("")
print(f"el color de la clase hija ees {hijita.color}")

regalon = Nieto(10)
panial = "XL"

hijito = Hijo(10, 1500)

super(type(hijita),hijita).cambiar_color("gris")
print(f"el color de la clase hija es {hijita.color}")

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"princesa es intancia de Hija: {isinstance(hijita,Hija)}") # True
print(f"princesa es intancia de Padre: {isinstance(hijita,Padre)}") # True
print(f"princesa es intancia de Madre: {isinstance(hijita,Hijo)}") # False