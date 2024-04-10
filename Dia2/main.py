from pelota import Pelota

#creacion de objeto o instancia de la clase
pelota_multicolor = Pelota()

#print(pelota_multicolor.color) AttributeError: 'Pelota' object has no attribute 'color'

pelota_multicolor.asigna_color("rojo")
print(pelota_multicolor.color)

pelota_multicolor.lee_color()

pelota_multicolor.asigna_color("verde")

pelota_multicolor.lee_color_local_y_atributo("amarillo")

pelota_negro = Pelota()
pelota_negro.lee_color_local_y_atributo("Negro") 
#print("El color de esta pelota es {}".format(self.color))
#                                                 ^^^^^^^^^^
#AttributeError: 'Pelota' object has no attribute 'color'