class Ticket:
    def __init__(self, identificador, descripcion, prioridad, canal, hora_llegada):
        self.identificador = identificador
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.canal = canal
        self.hora_llegada = hora_llegada


if __name__ == "__main__":
    t1 = Ticket(1, "No prende la impresora", "alta", "telefono", "09:05")
    print(t1.descripcion)
    print(t1.prioridad)
