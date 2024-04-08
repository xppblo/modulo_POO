#import pelota
from pelota import Pelota

#pelota_de_andy =  pelota.Pelota()
#Instancia del objeto
pelota_de_andy = Pelota()

print(pelota_de_andy) #<pelota.Pelota object at 0x000002302AF85EB0>
print(type(pelota_de_andy)) # <class 'pelota.Pelota'>

pelota_de_andy.material = "Plastico"

print(pelota_de_andy.material)