from medicamento import Medicamento

#Instancia de objeto o creacion de objeto
paracetamol = Medicamento()
aspirina = Medicamento()
ibuprofeno = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)

paracetamol.descuento = 0.06
print(paracetamol.descuento)

Medicamento.descuento = 0.04

precio = int(input("Ingrese el precio a validar > "))
es_valido = Medicamento.validar_mayor_0(precio)

if es_valido:
    print("El precio ingresado es valido")
else:
    print("El precio ingresado no es valido")
    
print(paracetamol.descuento, aspirina.descuento)
    
if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento :
    print(f"Los medicamentos tienen los mismos IVA {Medicamento.IVA} y descuentos {Medicamento.descuento} ")
else:
    print(f"el IVA de paracetamol es {paracetamol.IVA} y el de aspirina es {aspirina.IVA} , tambien el descuento es de {paracetamol.descuento} y {aspirina.descuento}")

Medicamento.IVA = 0.19
#ibuprofeno.modificar_atributo()
print(ibuprofeno.IVA)
print(aspirina.IVA)
print(aspirina.descuento, paracetamol.descuento)