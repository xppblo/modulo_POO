"""class MisExcepciones(Exception):
    
    def imprimir_promedio(self, dividendo, divisor):
        promedio = dividendo/divisor #ZeroDivisionError: division by zero
        print(f"el promedio es : {promedio}")
     
calculo_promedio = MisExcepciones()

calculo_promedio.imprimir_promedio(100,0)
"""
class Error(Exception):
    pass

class DivisorError(Error):
    def __init__(self, mensaje ,divisor):
        self.divisor = divisor
        self.mensaje = mensaje

class MisExcepciones(Exception):
    
    def imprimir_promedio(self, dividendo, divisor):
        try:
            promedio = dividendo/divisor #ZeroDivisionError: division by zero
            print(f"el promedio es : {promedio}")            
        except ValueError:
            print(f"Error en el ingreso de datos : {error}")
        except ZeroDivisionError as error:
            print("El divisor no puede ser 0")        
        except Exception as error:
            print(f"Se ha producido un error : {error}")
        
            
     
calculo_promedio = MisExcepciones()

dividendo = int(input("Ingrese el dividendo\n > "))

valido = True

while valido:
    try:
        divisor = int(input("ingrese el numero divisor > "))
        if divisor == 0:
            raise DivisorError("Divisor no puede ser cero",divisor)
        valido = False
    except DivisorError as de:
        print("Error en el ingreso del divisor",de.mensaje)
    except ValueError:
        print("Error en el ingreso del divisor")

calculo_promedio.imprimir_promedio(dividendo,divisor)