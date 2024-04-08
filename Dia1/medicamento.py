class Medicamento():
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_0(numero : int):
        return numero > 0
    
    @staticmethod
    def modificar_atributo():
        Medicamento.IVA = 0.19