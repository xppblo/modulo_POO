class Medicamento():
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_0(numero : int):
        return numero > 0
    
    #los metodos estaticos no pueden modificar los atributos de clase por si solos
    @staticmethod
    def modificar_atributo():
        Medicamento.IVA = 0.19