from medicamento import Medicamento

# Paso 1 es crear una instancia

medicamento_nuevo = Medicamento()

# Paso 2 solicitud de datos
precio = int(input("Ingrese el precio del medicamento > "))

# Paso 3 pasar al metodo de la instancia

medicamento_nuevo.asigna_precio(precio)

print(f"El precio es : {medicamento_nuevo.precio}")
print(f"El descuento es : {medicamento_nuevo.descuento}")

#No se puede llamar a un metodo no estatico como una clase
Medicamento.asigna_precio(precio) # TypeError: Medicamento.asigna_precio() missing 1 required positional argument: 'precio_entregado'