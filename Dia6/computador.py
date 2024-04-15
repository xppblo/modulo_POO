class Ram():
    def __init__(self):
        self.velocidad = 1500
        self.bite = 32

class DiscoDuro():
    def __init__(self):
        self.capacidad = 1024
        self.tipo = "ssd"
        
class Teclado():
    def __init__(self, idioma : str, cant_teclas : int):
        self.idioma = idioma
        self.cant_teclas = cant_teclas
        
class Mouse():
    def __init__(self, tipo : str, conectividad : str):
        self.tipo = tipo
        self.conectividad = conectividad

class Computador():
    #el computador esta compuesto de otras clases
    def __init__(self, teclado : Teclado, mouse : Mouse, velocidad_ram : Ram):
        self.ram = Ram(velocidad_ram,32) # composicion
        self.disco_duro = DiscoDuro(1024) # composicion
        
        self.teclado = teclado #agregacion
        self.mouse = mouse #agregacion

#IMPORTANTE -> Si se crea en una instacia de una clase, por atributos es composicion y si es por parametros es agregacion

#Instancia de clases    

teclado = Teclado("latino", 40)
mouse = Mouse("Gamer", "bluethoot")
computador_gamer = Computador(teclado, mouse)