from medicamento import Medicamento

#Instancia de objeto o creacion de objeto
paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)

paracetamol.descuento = 0.06
print(paracetamol.descuento)