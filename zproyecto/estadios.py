class Estadio:
    def __init__(self, id, nombre, capacidad, ubicacion, restaurantes): #restaurantes es una lista de objetos
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.restaurantes = restaurantes