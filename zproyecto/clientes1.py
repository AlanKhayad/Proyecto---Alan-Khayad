class Cliente1:
    def __init__(self, nombre, cedula, boletos=[]):
        self.nombre = nombre
        self.cedula = cedula
        self.boletos = boletos

    def append_boleto(self, boleto):
        self.boletos.append(boleto)

    def mostrar(self):
        print(f"\nNombre: {self.nombre}\nCédula: {self.cedula}\n{self.boletos}")