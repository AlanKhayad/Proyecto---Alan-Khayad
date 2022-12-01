import emoji

pepsi = emoji.emojize(":cup_with_straw:")
hamburger = emoji.emojize(":hamburger:")
fish = emoji.emojize(":fish:")
chips = emoji.emojize(":french_fries:")
water = emoji.emojize(":baby_bottle:")
beer = emoji.emojize(":beer_mug:")
pasta = emoji.emojize(":spaghetti:")
steak = emoji.emojize(":corte_de_carne:")
gatorade = emoji.emojize(":lotion_bottle:")

class Producto:
    def __init__(self, nombre, precio, tipo, inventario):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.inventario = inventario
        self.iva = precio * 0.16
        self.precio_neto = precio + self.iva

class Bebida(Producto):
    def __init__(self, nombre, precio, tipo, inventario, alcochol):
        super().__init__(nombre, precio, tipo, inventario)
        self.alcohol = alcochol
        self.iva = precio * 0.16
        self.precio_neto = precio + self.iva

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio_neto}\nUnidades disponibles: {self.inventario}\nAlcohólica: {self.alcohol}")

    def mostrar2(self):
        if self.nombre == "Pepsi":
           print(f"{self.nombre} {pepsi}  ({self.precio} $)")
        if self.nombre == "Hamburger":
           print(f"{self.nombre} {hamburger}  ({self.precio}) $")
        if self.nombre == "Water":
           print(f"{self.nombre} {water}  ({self.precio}) $")
        if self.nombre == "Beer":
           print(f"{self.nombre} {beer}  ({self.precio}) $")
        if self.nombre == "Steak":
           print(f"{self.nombre} {steak}  ({self.precio}) $")
        if self.nombre == "Pasta":
           print(f"{self.nombre} {pasta}  ({self.precio}) $")
        if self.nombre == "Gatorade":
           print(f"{self.nombre} {gatorade}  ({self.precio}) $")
        if self.nombre == "Fish and Chips":
           print(f"{self.nombre} {fish}  ({self.precio}) $")
               

    def cambiar_inv(self):
        self.inventario -= 1

class Comida(Producto):
    def __init__(self, nombre, precio, tipo, inventario, empa_prep):
        super().__init__(nombre, precio, tipo, inventario)
        self.empa_prep = empa_prep
        self.iva = precio * 0.16
        self.precio_neto = precio + self.iva

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nPrecio {self.precio_neto}\nUnidades disponibles: {self.inventario}\nTipo: {self.empa_prep}")

    def mostrar2(self):
        if self.nombre == "Pepsi":
           print(f"{self.nombre} {pepsi}  ({self.precio} $)")
        if self.nombre == "Hamburger":
           print(f"{self.nombre} {hamburger}  ({self.precio}) $")
        if self.nombre == "Water":
           print(f"{self.nombre} {water}  ({self.precio}) $")
        if self.nombre == "Beer":
           print(f"{self.nombre} {beer}  ({self.precio}) $")
        if self.nombre == "Steak":
           print(f"{self.nombre} {steak}  ({self.precio}) $")
        if self.nombre == "Pasta":
           print(f"{self.nombre} {pasta}  ({self.precio}) $")
        if self.nombre == "Gatorade":
           print(f"{self.nombre} {gatorade}  ({self.precio}) $")
        if self.nombre == "Fish and Chips":
           print(f"{self.nombre} {fish}  ({self.precio}) $")

    def cambiar_inv(self):
        self.inventario -= 1