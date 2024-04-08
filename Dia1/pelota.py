class Pelota():
    #atributo
    forma = "redonda"
    material = ""
    posiciones = [3,0,2,1,0]
    
    #metodo estatico
    @staticmethod
    def crear_rebote():
        return [5,0,4,0,3,0,2,0,1,0]
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)
        
    #metodo no estatico
    #modificacion de un estado del "Objeto"
    def rebotar(self):
        self.posiciones = self.crear_rebote()
        
    
    def nuevo_atributo(self):
        self.color = "blanco"