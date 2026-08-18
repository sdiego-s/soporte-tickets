from ticket import Ticket


class ColaPrioridad:
    def __init__(self):
        self.tickets = []
        self.prioridades = {"alta": 1, "media": 2, "baja": 3}

    def agregar_ticket(self, ticket):
        self.tickets.append(ticket)

    def atender_siguiente(self):
        if not self.tickets:
            raise ValueError("La cola esta vacía")
        siguiente = min(
            self.tickets, key=lambda t: (self.prioridades[t.prioridad], t.hora_llegada)
        )
        self.tickets.remove(siguiente)
        return siguiente


if __name__ == "__main__":
    cola = ColaPrioridad()
    cola.agregar_ticket(Ticket(1, "Problema con correo", "media", "internet", "09:00"))
    cola.agregar_ticket(Ticket(2, "Servidor caído", "alta", "telefono", "09:05"))
    cola.agregar_ticket(Ticket(3, "No conecta VPN", "alta", "presencial", "09:10"))
    cola.agregar_ticket(Ticket(4, "Duda de facturación", "baja", "internet", "09:15"))
    siguiente = cola.atender_siguiente()
    print(f"Atender: Ticket {siguiente.identificador} - {siguiente.descripcion}")
