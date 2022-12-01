class Boleto:
    def __init__(self, nombre, cedula, edad, partido, tipo_entrada, asiento, id_entrada, precio_ticket, gasto_rest, asistencia):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido
        self.tipo_entrada = tipo_entrada
        self.asiento = asiento
        self.id_entrada = id_entrada
        self.precio_ticket = precio_ticket
        self.gasto_rest = gasto_rest
        self.asistencia = asistencia

    def act_gasto_rest(self, gasto):
        self.gasto_rest += gasto

    def asistio(self):
        self.asistencia = True

    def añadir_asiento(self, asiento):
        self.asiento.append(asiento)