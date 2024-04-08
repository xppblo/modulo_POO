#import pelota
from pelota import Pelota

#pelota_de_andy =  pelota.Pelota()
#Instancia del objeto
pelota_de_andy = Pelota()

print(pelota_de_andy) #<pelota.Pelota object at 0x000002302AF85EB0>
print(type(pelota_de_andy)) # <class 'pelota.Pelota'>

pelota_de_andy.material = "Plastico"

print(pelota_de_andy.material)

pelota_tenis = Pelota()
pelota_tenis.material = "Caucho"

#metodos eestaticos
#no se necesita un objeto para llamar al metodo
print(Pelota.crear_rebote) #<function Pelota.crear_rebote at 0x000001806A2DDC60>
print(Pelota.crear_rebote()) # (5, 0, 4, 0, 3, 0, 2, 0, 1, 0)

Pelota.imprimir_posiciones() # [3, 0, 2, 1, 0]

pelota_fultbol = Pelota()

# metodo no estatico
pelota_fultbol.rebotar()
print(pelota_fultbol.posiciones) # [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

pelota_basketball = Pelota()
print(pelota_basketball.posiciones)# [3, 0, 2, 1, 0]
#metodo no estatico, permiten crear atributos(variables) de tipos "atributos de instancia"
pelota_basketball.nuevo_atributo() 
print(pelota_basketball.color) # blanco
#print(pelota_fultbol.color) # AttributeError: 'Pelota' object has no attribute 'color'