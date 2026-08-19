from ticket import Ticket


class ColaPrioridad:
    def __init__(self):
        self.tickets = []
        self.prioridades = {"alta": 1, "media": 2, "baja": 3}
        self.siguiente_id = 1

    def agregar_ticket(self, descripcion, prioridad, canal, hora_llegada):
        ticket = Ticket(
            self.siguiente_id,
            descripcion,
            prioridad.lower().strip(),
            canal.lower().strip(),
            hora_llegada,
        )
        self.tickets.append(ticket)
        self.siguiente_id += 1

    def atender_siguiente(self):
        if not self.tickets:
            raise ValueError("La cola esta vacía")
        siguiente = min(
            self.tickets, key=lambda t: (self.prioridades[t.prioridad], t.hora_llegada)
        )
        self.tickets.remove(siguiente)
        return siguiente

    def ver_cola(self):
        cola_Ordenada = sorted(
            self.tickets,
            key=lambda t: (self.prioridades[t.prioridad], t.hora_llegada),
        )
        return cola_Ordenada


if __name__ == "__main__":
    cola = ColaPrioridad()
    cola.agregar_ticket("Problema con correo", "media", "internet", "09:00")
    cola.agregar_ticket("Servidor caído", "alta", "telefono", "09:05")
    cola.agregar_ticket("No conecta VPN", "alta", "presencial", "09:10")
    cola.agregar_ticket("Duda de facturación", "baja", "internet", "09:15")

    siguiente = cola.atender_siguiente()
    print(f"Atender: Ticket {siguiente.identificador} - {siguiente.descripcion}")

    print("\nCola completa ordenada:")
    for t in cola.ver_cola():
        print(f"  [{t.identificador}] {t.prioridad} - {t.descripcion}")
