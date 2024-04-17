from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

#HECO CON AYUDA DE CHATGPT 

def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    return Producto(nombre, precio, stock)

def menu():
    print("\n--- Menú ---")
    print("1. Listar productos")
    print("2. Realizar venta")
    print("3. Salir")

def main():
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ")

    if tipo_tienda.lower() == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    continuar_ingresando = True
    while continuar_ingresando:
        producto = ingresar_producto()
        tienda.ingresar_producto(producto)
        opcion = input("¿Desea ingresar otro producto? (si/no): ")
        if opcion.lower() != "si":
            continuar_ingresando = False

    continuar_programa = True
    while continuar_programa:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Productos disponibles:")
            print(tienda.listar_productos())
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.vender_producto(nombre_producto, cantidad)
        elif opcion == "3":
            continuar_programa = False
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
