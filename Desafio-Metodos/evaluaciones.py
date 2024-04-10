from pizza import Pizza

#punto a
print(f"Este es el precio de las pizzas ${Pizza.precio} y todas son de tamaño {Pizza.tamano}")

#punto b
print(Pizza.validar_elemento("salsa de tomate",["salsa de tomate","salsa bbq"]))

#punto c
pizza = Pizza()
print("")
pizza.realizar_pedido()

if pizza.es_pizza_valida:
    print("")
    print("Estos son los ingredientes de su pizza")
    print(f"Ingrediente proteico : {pizza.proteico}")
    print(f"Ingredientes vegetales : {pizza.vegetales[0]} - {pizza.vegetales[1]}")
    print(f"Tipo de maza : {pizza.masa}")
else:
    print("La pizza no es valida")

#print(Pizza.es_pizza_valida) AttributeError: type object 'Pizza' has no attribute 'es_pizza_valida'