class Medicamento():
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_0(numero : int):
        return numero > 0
            
    def asigna_precio(self, precio_entregado: int):
        es_valido = self.validar_mayor_0(precio_entregado)
        if es_valido:
            self.precio = precio_entregado
            self.descuento = 0.0
            if self.precio >= 10000 and self.precio < 20000:
                self.descuento = 0.1
            elif self.precio >= 20000 and self.precio < 30000:
                self.descuento = 0.2
            elif self.precio >= 30000:
                self.descuento = 0.3
        else:
            print(f"El precio {precio_entregado}, no es un precio válido")