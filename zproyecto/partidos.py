class Partido:
    def __init__(self, local, visitante, fecha, estadio, id, asientos_ocup, asistencia):
        self.local = local
        self.visitante = visitante
        self.fecha = fecha
        self.estadio = estadio
        self.id = id
        self.asientos_ocup = asientos_ocup
        self.asistencia = asistencia

    def mostrar_datos(self):
        print(f"{self.local.nombre} VS {self.visitante.nombre}\nFecha: {self.fecha}\nEstadio: {self.estadio.nombre}\nId: {self.id}")

    def mostrar_datos_2(self):
        if len(self.asientos_ocup) != 0:
            print(f"{self.local.nombre} VS {self.visitante.nombre}\nFecha: {self.fecha}\nEstadio: {self.estadio.nombre}\nBoletos vendidos: {len(self.asientos_ocup)}\nAsistencias: {self.asistencia}\nAsistencia/Venta: {round(self.asistencia/len(self.asientos_ocup),2)}")
        else:
            print(f"{self.local.nombre} VS {self.visitante.nombre}\nFecha: {self.fecha}\nEstadio: {self.estadio.nombre}\nBoletos vendidos: {len(self.asientos_ocup)}\nAsistencias: {self.asistencia}\nAsistencia/Venta: 0")