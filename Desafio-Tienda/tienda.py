from abc import ABC, abstractmethod

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def get_nombre(self):
        return self.__nombre

    def get_costo_delivery(self):
        return self.__costo_delivery

    def get_productos(self):
        return self.__productos

    @abstractmethod
    def ingresar_producto(self, producto):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def vender_producto(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        # Los productos del restaurante se crean al vender, no al ingresar.
        pass

    def listar_productos(self):
        return "No hay productos disponibles para listar en un restaurante."

    def vender_producto(self, nombre_producto, cantidad):
        # Los productos del restaurante se crean al vender.
        pass

class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        encontrado = False
        for prod in self.get_productos():
            if prod.get_nombre() == producto.get_nombre():
                prod.set_stock(prod.get_stock() + producto.get_stock())
                encontrado = True
                break
        if not encontrado:
            self.get_productos().append(producto)

    def listar_productos(self):
        lista_productos = ""
        for producto in self.get_productos():
            stock_info = f" (Pocos productos disponibles)" if producto.get_stock() < 10 else ""
            lista_productos += f"{producto.get_nombre()} - ${producto.get_precio()}{stock_info}\n"
        return lista_productos

    def vender_producto(self, nombre_producto, cantidad):
        for prod in self.get_productos():
            if prod.get_nombre() == nombre_producto:
                if prod.get_stock() >= cantidad:
                    prod.set_stock(prod.get_stock() - cantidad)
                else:
                    prod.set_stock(0)
                break

class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        encontrado = False
        for prod in self.get_productos():
            if prod.get_nombre() == producto.get_nombre():
                prod.set_stock(prod.get_stock() + producto.get_stock())
                encontrado = True
                break
        if not encontrado:
            self.get_productos().append(producto)

    def listar_productos(self):
        lista_productos = ""
        for producto in self.get_productos():
            envio_gratis = f" (Envío gratis al solicitar este producto)" if producto.get_precio() > 15000 else ""
            lista_productos += f"{producto.get_nombre()} - ${producto.get_precio()}{envio_gratis}\n"
        return lista_productos

    def vender_producto(self, nombre_producto, cantidad):
        for prod in self.get_productos():
            if prod.get_nombre() == nombre_producto:
                if cantidad <= 3 and prod.get_stock() >= cantidad:
                    prod.set_stock(prod.get_stock() - cantidad)
                elif cantidad > 3 and prod.get_stock() >= 3:
                    prod.set_stock(prod.get_stock() - 3)
                else:
                    prod.set_stock(0)
                break
