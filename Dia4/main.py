from pelota import Pelota

nueva_pelota= Pelota("Negro")

nueva_pelota.setColor("Blanco")
print(nueva_pelota.color)

nueva_pelota.color = "Naranjo"
print(nueva_pelota.color)

nueva_pelota.__password= "admin1234"
#print(nueva_pelota.__password)

#nueva_pelota.color = ""
#print(nueva_pelota.color)#Verde

nueva_pelota.color
print(nueva_pelota.color)